FROM alpine@sha256:fa1b3b8cd12d2b2ded5ef366f99b5a7556884646af680404989d626535a3ac14

RUN apk update && apk add tidyhtml
COPY tidy.config /

ENTRYPOINT ["tidy", "-config", "tidy.config"]
