FROM alpine@sha256:a2d49ea686c2adfe3c992e47dc3b5e7fa6e6b5055609400dc2acaeb241c829f4

RUN apk update && apk add tidyhtml
COPY tidy.config /

ENTRYPOINT ["tidy", "-config", "tidy.config"]
