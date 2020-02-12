docker run --mount src=myorgfiles,dst=/tmp/scratch ubuntu find /tmp/scratch -type f -name '*.org' | cat -n -

docker run --mount src=myorgfiles,dst=/tmp/scratch ubuntu find /tmp/scratch -type f -not -name '*.org' | wc -l
