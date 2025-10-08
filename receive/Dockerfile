FROM python:3.13-alpine@sha256:359453e628fce9b2e02785f440c587b6aca219ac957ae8388fcfb8bcdee7c7ef

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
