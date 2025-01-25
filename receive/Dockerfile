FROM python:3.13-alpine@sha256:be540041682c83228415ca1dbdb061d78d6994523e8ff79c5d5b2a5cab56effb

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
