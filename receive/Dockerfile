FROM python:3.14-alpine@sha256:e1a567200b6d518567cc48994d3ab4f51ca54ff7f6ab0f3dc74ac5c762db0800

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
