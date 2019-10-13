FROM alpine

RUN apk update && apk add tidyhtml
COPY tidy.config /

ENTRYPOINT ["tidy", "-config", "tidy.config"]
