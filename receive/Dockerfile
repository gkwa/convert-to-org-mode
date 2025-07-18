FROM python:3.13-alpine@sha256:37b14db89f587f9eaa890e4a442a3fe55db452b69cca1403cc730bd0fbdc8aaf

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
