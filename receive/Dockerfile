FROM python:3.13-alpine@sha256:bd8f7ae071e5aad0b84264df205f5a156a777652cf4a20583c9f765883f424b9

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
