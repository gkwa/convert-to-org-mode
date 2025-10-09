FROM python:3.14-alpine@sha256:9c32c2f24d00536cac7d4d356d82c5274fb17366c52aa59ed0cc4c06f8b60a35 as base
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
