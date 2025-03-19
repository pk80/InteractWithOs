#!/usr/bin/env bash

line="-------------------------------"

echo $line
echo "While Loop"
echo $line
n=1
while [ $n -le 5 ]; do
	echo "Iteration number $n"
	((n+=1))
done;

echo $line
echo "Retry"
echo $line
n=0
command=$1
while ! $command && [ $n -le 5 ]; do
	sleep $n
	((n+=1))
	echo "Retry #$n"
done;

echo $line
echo "For Loop"
echo $line
for fruit in peach orange pear; do
	echo "I like $fruit"
done
