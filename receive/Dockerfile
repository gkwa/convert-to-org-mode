FROM python:3.13-alpine@sha256:f9d772b2b40910ee8de2ac2b15ff740b5f26b37fc811f6ada28fce71a2542b0e

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
