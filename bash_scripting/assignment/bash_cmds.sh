#!/usr/bin/env bash

line="------------------------------------------------------------------------------------------"

echo $line
echo "Lines which include 'jane'" 
echo $line
grep 'jane' list.txt

echo $line
echo "Lines which include only ' jane '"
echo $line
grep ' jane ' list.txt

echo $line ; echo "cut with grep : first field by separating with space" ; echo $line
grep ' jane ' list.txt | cut -d ' ' -f 1
grep ' jane ' list.txt | cut -d ' ' -f 2
grep ' jane ' list.txt | cut -d ' ' -f 1
grep ' jane ' list.txt | cut -d ' ' -f 1-3

echo $line ; echo "test command to test for presence of file" ; echo $line
file=list.txt
if test -e $file; then
	echo "File exists : $file"
else
	echo "File $file doesn't exist"
fi

echo $line ; echo "Redirection operator" ; echo $line
> test.txt
echo "file test.txt is created"
echo "I am appending text to this test file" >> test.txt
cat test.txt

echo $line; echo "Iterations: for, while, until"; echo $line
for i in 1 2 3;do echo "Iteration $i"; done

echo $line; echo "Finding 'jane' files using bash script"; echo $line
> jane_files.txt
files=$(grep " jane " list.txt | cut -d ' ' -f 3)
for file in $files; do
	# if test -e "$(file)"; then echo "($file)" >> jane_files.txt; fi
  echo "${file}" >> jane_files.txt
done
echo "Files written to jane_files.txt"

echo $line
