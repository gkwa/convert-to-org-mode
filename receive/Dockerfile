FROM python:3.13-alpine@sha256:5b55b4912097e5c297584c6d041fdf94941f8c46a47e488f01556ac066353a41

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
