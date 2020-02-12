FROM python:3.8-alpine

WORKDIR /tmp

COPY . .

ENTRYPOINT ["python", "cleanup.py"]
CMD [ "--path", "/tmp" ]
