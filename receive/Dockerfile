FROM python:3.13-alpine@sha256:0df5d0fed7583b14e7761a58c8bcb7444c5c520245ad3f1a346a7beafcf6ade5

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
