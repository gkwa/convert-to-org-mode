FROM python:3.13-alpine@sha256:dfb9a4d4dead8fde38a19f124d02c7345cac853b5bcaeff9c0334f8344c47f18 as base
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
