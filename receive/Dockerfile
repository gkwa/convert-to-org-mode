FROM python:3.13-alpine@sha256:5dad625efcbc6fad19c10b7b2bfefa1c7a8129c8f8343106b639c27dd9e7db2c

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
