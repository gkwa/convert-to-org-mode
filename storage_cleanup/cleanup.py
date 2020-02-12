import argparse
import datetime
import pathlib

parser = argparse.ArgumentParser(description="Short sample app")
parser.add_argument("path", help="please provide filename/filepath")
args = parser.parse_args()

mydir = pathlib.Path(args.path)

all_ = set(mydir.glob("*"))
org = set(mydir.glob("*.org"))
destroy = set()

now = datetime.datetime.now()
for path in all_:
    if not path.is_file():
        continue
    mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
    diff = now - mtime
    if diff > datetime.timedelta(days=1):
        destroy.add(path)

# keep org files
destroy -= org

# delete org files older than 30 days
for path in org:
    mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
    diff = now - mtime
    if diff > datetime.timedelta(days=30):
        destroy.add(path)

for file in destroy:
    file.unlink()
