FROM python:3.13-alpine@sha256:5dcc4bdd33c7ed3a43d64495fb83bb38653ab5cd776dd97e63e9b6499fc8fc89 as base
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
