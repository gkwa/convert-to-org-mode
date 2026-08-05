FROM python:3.14-alpine@sha256:b0509bdcd664f2c819942bd9375038bb59c8126962d2f4cf588cc5683ef149cd

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
