FROM alpine

ENTRYPOINT find /tmp/scratch -mtime +7 -type f -not -name *.org -delete
