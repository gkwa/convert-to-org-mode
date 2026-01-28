FROM python:3.14-alpine@sha256:c97d6e916998ebe4e08c44ca85a15abe70d084e6be803f19ffd59116725953ef

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
