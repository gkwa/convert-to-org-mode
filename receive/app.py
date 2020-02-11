import base64
import pathlib
import re
import shutil
import string
import subprocess

import contractions
import flask

import flask_cors

app = flask.Flask(__name__)
cors = flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})


def tidy(html_path, tidy_path):
    cmd = [
        "docker",
        "run",
        "--mount",
        f"src={html_path.parent},dst={html_path.parent}",
        "convert-to-org-mode_tidy",
        "-file",
        str(html_path.parent.joinpath(f"{html_path.stem}-tidy-errors.log")),
        str(html_path),
    ]

    app.logger.debug(" ".join(cmd))
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=html_path.parent
    )
    _, stderr = process.communicate()
    if stderr:
        app.logger.warning(stderr)


def tidy2(html_path):
    cmd = [
        "docker",
        "run",
        "--mount",
        f"src={html_path.parent},dst={html_path.parent}",
        "convert-to-org-mode_tidy",
        "-file",
        str(html_path.parent.joinpath(f"{html_path.stem}-tidy-errors2.log")),
        str(html_path),
    ]

    app.logger.debug(" ".join(cmd))
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=html_path.parent
    )
    _, stderr = process.communicate()
    if stderr:
        app.logger.warning(stderr)


def mime_to_html(data, mime_path, html_path, html_path_orig):
    """ convert back from base64 to UTF-8 or ISO-8859-1 """

    text = ""
    try:
        text = base64.b64decode(data).decode(encoding="UTF-8")

    except UnicodeDecodeError as ex:
        app.logger.exception(ex)
        text = base64.b64decode(data).decode(encoding="ISO-8859-1")

    html_path.write_text(text)
    html_path_orig.write_text(text)
    app.logger.debug(f"{html_path.resolve()} written")


def miscellaneous_html_updates(html_path, url):
    cmd = [
        "docker",
        "run",
        "--mount",
        f"src={html_path.parent},dst={html_path.parent}",
        "convert-to-org-mode_pandoc_cleanup",
        "--html",
        str(html_path),
        "--fix-html",
        "--url",
        url,
    ]
    app.logger.debug(" ".join(cmd))
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=html_path.parent
    )
    _, stderr = process.communicate()
    if stderr:
        app.logger.warning(stderr)


def generate_org(html_path, org_path):
    cmd = [
        "docker",
        "run",
        "--mount",
        f"src={html_path.parent},dst={html_path.parent}",
        "pandoc/core",
        "--from=html",
        "--to=org",
        f"--output={str(org_path)}",
        str(html_path),
    ]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=html_path.parent
    )
    _, stderr = process.communicate()
    app.logger.debug(" ".join(cmd))


def pandoc_cleanup_org(org_path):
    cmd = [
        "docker",
        "run",
        "--mount",
        f"src={org_path.parent},dst={org_path.parent}",
        "convert-to-org-mode_pandoc_cleanup",
        "--org",
        str(org_path),
    ]
    app.logger.debug(" ".join(cmd))
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=org_path.parent
    )
    _, stderr = process.communicate()
    if stderr:
        app.logger.warning(stderr)


def emacs_cleanup_org(org_path):
    cmd = [
        "docker",
        "run",
        "--mount",
        f"src={org_path.parent},dst={org_path.parent}",
        "convert-to-org-mode_emacs_cleanup",
        "-f",
        str(org_path),
    ]
    app.logger.debug(" ".join(cmd))
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=org_path.parent
    )
    _, stderr = process.communicate()
    if stderr:
        app.logger.warning(stderr)


def generate_filename_stem(title, host):
    stem = f"app-{host}-{title}"
    keep = string.ascii_letters + string.digits + " "

    stem = stem.lower()
    stem = contractions.expandContractions(stem)

    # replace non-keep characters with hyphen
    stem = re.sub(f"[^{keep}]", "-", stem)
    stem = re.sub(" ", "-", stem)
    stem = re.sub("-{2,}", "-", stem)
    stem = stem[:100]
    stem = re.sub("-+$", "", stem)
    return stem


@app.route("/healthcheck")
def healthcheck():
    resp = flask.jsonify(success=True)
    return resp


@app.route("/", methods=["POST"])
def save_and_process():
    if flask.request.method == "POST":
        content = flask.request.get_json()

        url = content["url"]
        host = content["host"]
        data = content["data"]
        title = content["title"]

        stem = generate_filename_stem(title, host)

        scratch_dir = pathlib.Path("/tmp/scratch").resolve()
        mime_path = scratch_dir / f"{stem}.mime"
        html_path_orig = scratch_dir / f"{stem}-orig.html"
        html_path = scratch_dir / f"{stem}.html"
        org_path = scratch_dir / f"{stem}.org.tmp"
        org_path_final = scratch_dir / f"{stem}.org"
        tidy_path = scratch_dir / f"{stem}-tidy.html"

        scratch_dir.mkdir(exist_ok=True)
        mime_path.write_text(data)
        mime_to_html(data, mime_path, html_path, html_path_orig)
        tidy(html_path, tidy_path)
        shutil.copy(str(html_path), str(tidy_path))
        miscellaneous_html_updates(html_path, url)
        tidy2(html_path)
        generate_org(html_path, org_path)
        pandoc_cleanup_org(org_path)
        emacs_cleanup_org(org_path)
        shutil.move(str(org_path), str(org_path_final))

    resp = flask.jsonify(success=True)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
