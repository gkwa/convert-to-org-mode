FROM python:3.14-alpine@sha256:0bf59161c735f604ea070af402d65b1a088ce3fd7fe4329f5983446148e84930

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
