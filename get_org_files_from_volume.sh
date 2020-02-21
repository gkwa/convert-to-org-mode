#!/bin/sh

set -e

set +e
docker rm orgstore
set -e

docker run --mount src=myorgfiles,dst=/tmp/scratch --name orgstore ubuntu /bin/bash
docker run --rm --volumes-from orgstore -v $(pwd):/backup ubuntu tar -cf /backup/backup.tar /tmp/scratch/
tar --delete -f backup.tar --wildcards tmp/scratch/*{.html,.log,.mime}
docker run --mount src=myorgfiles,dst=/tmp/scratch ubuntu find /tmp/scratch -type f -name '*.org' -delete
docker run --mount src=myorgfiles,dst=/tmp/scratch ubuntu find /tmp/scratch -type f -name '*.org' | cat -n -
tar xf backup.tar
du -shc tmp/scratch
