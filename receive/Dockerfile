FROM python:3.13-alpine@sha256:7ef7abb375a9147c398e81abff9ecf0647e682b55e848f64344223c7987b8d37

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
