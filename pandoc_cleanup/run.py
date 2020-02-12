import argparse
import datetime
import logging
import pathlib

import transform

self_path = pathlib.Path(__file__).resolve()

logger = logging.getLogger(f"{self_path.stem}")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(f"{self_path.stem}.log")
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

parser = argparse.ArgumentParser(description="Short sample app")
parser.add_argument("--url", action="store")
parser.add_argument("--html", default="out.html", action="store")
parser.add_argument("--org", action="store")
parser.add_argument("--fix-html", action="store_true")
args = parser.parse_args()
html_path = pathlib.Path(args.html)

if args.fix_html:
    html = html_path.read_text()
    html = transform.customize(html, args.url)
    html_path.write_text(html)

if args.org:
    org_path = pathlib.Path(args.org)
    text = transform.transform(org_path.read_text())
    #    logger.debug(f"writing to {org_path.resolve()}")
    org_path.write_text(text)


mydir = html_path.parent
now = datetime.datetime.now()
for_keeps = set(".org")

for path in mydir.glob("*"):
    mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
    age = now - mtime
    is_directory = not path.is_file()
    if is_directory:
        continue

    is_young = age <= datetime.timedelta(minutes=10)
    if is_young:
        continue

    is_keep_worthy = path.suffix.lower() in for_keeps and age <= datetime.timedelta(days=7)
    if is_keep_worthy:
        continue

    path.unlink()
