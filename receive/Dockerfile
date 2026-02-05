FROM python:3.14-alpine@sha256:14558bb88225c495de95c0796c22de2c708500e48e9a6b84ce6b729d590fcb65

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
