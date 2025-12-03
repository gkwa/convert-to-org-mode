FROM python:3.14-alpine@sha256:d7fb7df19ca613dcebf0969d0ab2b04bb35e95f325c104da1b1718162468f6de

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
