FROM python:3.13-alpine@sha256:3e7ba24f47ca46dca3491b35db5c2f33c43fa932568a3577783839bbfc528e9d

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
