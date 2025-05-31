FROM python:3.13-alpine@sha256:a9bceef1fb20825c4f4c28eca616e5c1497bec444ea31205cc667b0b962fd9df

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
