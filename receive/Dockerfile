FROM python:3.14-alpine@sha256:961b74dee425a9c6446d4cc249a1337bf2f6f762865662c1e4f05a84de4940fd

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
