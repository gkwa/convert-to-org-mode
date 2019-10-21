#!/bin/bash

usage="$(basename "$0") [-h] [-s n] -- program to calculate the answer to life, the universe and everything

where:
    -h  show this help text
    -f  set the filename"

filename=""
while getopts ':hf:' option; do
    case "$option" in
    h)
        echo "$usage"
        exit
        ;;
    f)
        filename=$OPTARG
        ;;
    :)
        printf "missing argument for -%s\n" "$OPTARG" >&2
        echo "$usage" >&2
        exit 1
        ;;
    \?)
        printf "illegal option: -%s\n" "$OPTARG" >&2
        echo "$usage" >&2
        exit 1
        ;;
    esac
done
shift $((OPTIND - 1))

emacs --batch $filename \
    --load org \
    --load /user-init-org-mtmonacelli-utils.el \
    --eval '(org-mode)' \
    --eval '(reformat-paragraph-with-line-spacing-to-end-of-file)' \
    --funcall save-buffer
