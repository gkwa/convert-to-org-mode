FROM python:3.13-alpine@sha256:2c39ec94d4a87a074cced458da07865b427c5767e18f86e0fef59ce874d5c2e3

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
