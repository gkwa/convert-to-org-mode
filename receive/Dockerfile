FROM python:3.13-alpine@sha256:f50e1ca5ac620527f8a8acc336cab074dc8a418231380cd6d9eafb4103931f91

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
