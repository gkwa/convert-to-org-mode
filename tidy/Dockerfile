FROM alpine@sha256:71e9b7bae160ba167fa17414401b94cbcdaf3c32feeab9298bd794a2a0614c35

RUN apk update && apk add tidyhtml
COPY tidy.config /

ENTRYPOINT ["tidy", "-config", "tidy.config"]
