FROM python:3.14-alpine@sha256:5f1ff369fb05e17a9b569a7d92488607c49514e958101ca8a2290fd0fa52cdaf

RUN pip install --upgrade pip

RUN apk update && apk add docker-cli

COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
