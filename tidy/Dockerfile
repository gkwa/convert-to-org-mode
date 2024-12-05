FROM alpine@sha256:5cc1526ee5c99c2982793abe22861e6047cfb5c8609cbe2d6bbe11d836263354

RUN apk update && apk add tidyhtml
COPY tidy.config /

ENTRYPOINT ["tidy", "-config", "tidy.config"]
