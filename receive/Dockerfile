FROM python:3.13-alpine@sha256:bfd74f8005463fabde28a198bd772a26ef2a92585c9d1be8cb2e8cf54f7d61a9

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
