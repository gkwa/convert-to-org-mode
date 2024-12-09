FROM python:3.13-alpine@sha256:5dcc4bdd33c7ed3a43d64495fb83bb38653ab5cd776dd97e63e9b6499fc8fc89

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
