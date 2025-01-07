FROM python:3.13-alpine@sha256:992c45b1cf7affc93ff4aea53b28afb6921065bccb05b84cb69ac83475a7227c as base
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
