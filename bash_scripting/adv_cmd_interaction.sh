#!/usr/bin/env bash

for logfile in *log.txt;do
	echo "Processing: $logfile"
	cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
