FROM python:3.13-alpine@sha256:992c45b1cf7affc93ff4aea53b28afb6921065bccb05b84cb69ac83475a7227c

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
