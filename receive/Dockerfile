FROM python:3.13-alpine@sha256:dfb9a4d4dead8fde38a19f124d02c7345cac853b5bcaeff9c0334f8344c47f18

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
