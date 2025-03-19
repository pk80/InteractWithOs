#!/usr/bin/env bash


if grep "127\.0\.0\.1" /etc/hosts; then
    echo "Everything Ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

if test -n "$PATH"; then echo "Your path is not empty"; fi

if [ -n "$PATH" ]; then echo "Your path is not at all empty"; fi
