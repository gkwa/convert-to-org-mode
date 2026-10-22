FROM python:3.15-alpine@sha256:a58bff94159509f3a3f774da8c244001b74e0348139c421956abf991bfc9f1b8

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
