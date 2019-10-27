import base64
import pathlib
import re
import string

import contractions
import flask

import flask_cors

app = flask.Flask(__name__)
cors = flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})


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


def generate_filename_stem(base):
    stem = base

    stem = stem.lower()
    stem = contractions.expandContractions(stem)

    # replace non-keep characters with hyphen
    keep = string.ascii_letters + string.digits + " "
    stem = re.sub(f"[^{''.join({keep})}]", "-", stem)
    stem = stem.replace(" ", "-")
    stem = f"app-{stem}"
    stem = re.sub("-{2,}", "-", stem)
    stem = stem[:70]
    stem = re.sub("-+$", "", stem)
    return stem


@app.route("/", methods=["POST"])
def save_and_process():
    if flask.request.method == "POST":
        content = flask.request.get_json()

        data = content["data"]
        title = content["title"]

        stem = generate_filename_stem(title)

        scratch_dir = pathlib.Path("/tmp/scratch").resolve()
        mime_path = scratch_dir / f"{stem}.mime"
        html_path_orig = scratch_dir / f"{stem}-orig.html"
        html_path = scratch_dir / f"{stem}.html"

        scratch_dir.mkdir(exist_ok=True)
        mime_path.write_text(data)
        mime_to_html(data, mime_path, html_path, html_path_orig)

    resp = flask.jsonify(success=True)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
