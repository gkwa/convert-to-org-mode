import argparse
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
all_ = set(mydir.glob("*"))
keep = set(mydir.glob("*.org"))
destroy = all_ - keep
print(destroy)
for file in destroy:
    file.unlink()
