FROM python:3.14-alpine@sha256:508f7edacc36c9bdb5347020e0a55768ab0e4320be19dbd64d0a74c9939a7152

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
