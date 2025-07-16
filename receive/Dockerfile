FROM python:3.13-alpine@sha256:d005934d99924944e826dc659c749b775965b21968b1ddb10732f738682db869

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
