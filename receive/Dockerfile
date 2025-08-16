FROM python:3.13-alpine@sha256:8e4890b7d6e736b52bee1424d1bfaaa05145abbe626ea876d6770441e2bdf587

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
