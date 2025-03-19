#!/usr/bin/env bash

for file in *.txt; do
	name=$(basename "$file" .txt)
	mv "$file" "$name.csv"
	echo mv "$file" "$name.csv"
done
