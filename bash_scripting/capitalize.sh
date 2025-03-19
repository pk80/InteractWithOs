#!/usr/bin/env bash

for i in $(cat sample.txt); do
    B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`
    echo -n "${B}${i:1} ";
done
echo -e "\n"