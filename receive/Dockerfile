FROM python:3.14-alpine@sha256:c5c72336b2060db658391424c48466341838860a9f30efee9280ee53580d9537

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
