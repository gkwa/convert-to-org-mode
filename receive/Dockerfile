FROM python:3.13-alpine@sha256:2caf5deceb981f10dcc02e0cb8483b4abb15e7e48386683865e47fa52e878f35

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
