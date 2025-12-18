FROM python:3.14-alpine@sha256:7c2135f3b4c04e61b8e42c8a3149f520b55b5543cda68f1b879d419727347772

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
