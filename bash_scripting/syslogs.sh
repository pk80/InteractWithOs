#!/usr/bin/env bash
line="-------------------------------------------------------------------------------------------"

for logfile in /var/log/*.log; do
	echo $line
	echo "Processing $logfile"; echo $line
	tail $logfile
	# cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
