FROM python:3.14-alpine@sha256:2a77c2640cc80f5506babd027c883abc55f04d44173fd52eeacea9d3b978e811

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
