FROM python:3.13-alpine@sha256:a70b35b575e33d951e3f9d3fe94163ef0fd338c22552bc587a1b098a87ed6184

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
