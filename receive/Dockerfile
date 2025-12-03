FROM python:3.14-alpine@sha256:cc95388e96eeaa0a7dbf78d51d0d567cc0e9e2ae3ead2637877858de9b41a7bf

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
