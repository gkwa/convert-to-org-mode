FROM python:3.14-alpine@sha256:829edcc737417f9084a154511bde03a50b7996f3746e4c8a6b30a99a9a10648c

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
