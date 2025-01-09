FROM python:3.13-alpine@sha256:4ecc1be699f33ab3051ae8ec9532a77d1bf075739b1269b253cf3906a922f74e

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
