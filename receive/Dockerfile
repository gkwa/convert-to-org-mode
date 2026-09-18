FROM python:3.14-alpine@sha256:016508ba505da24f7139765bc4bb669df4e88eb2f12eeadd571bf2f88d7533df

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
