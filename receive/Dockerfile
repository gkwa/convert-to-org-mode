FROM python:3.15-alpine@sha256:d499023466546cd88a358f80b46fba4016f32597bc4482bb1c47b483a07d457d

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
