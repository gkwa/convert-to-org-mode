FROM python:3.8-alpine as base
FROM base as builder

RUN pip install --upgrade pip

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY run.py /
COPY transform.py /

ENTRYPOINT ["python","/run.py"]
CMD ["--help"]
