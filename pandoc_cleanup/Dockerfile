FROM python:3.13-alpine@sha256:a9bceef1fb20825c4f4c28eca616e5c1497bec444ea31205cc667b0b962fd9df as base
FROM base as builder

RUN pip install --upgrade pip

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY run.py /
COPY transform.py /

ENTRYPOINT ["python","/run.py"]
CMD ["--help"]
