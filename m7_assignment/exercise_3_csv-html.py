#!/usr/bin/env python3

import sys

csv_file=sys.argv[1]
html_file=sys.argv[2]

print(csv_file) 
print(html_file)

with open(html_file,'w') as file:
	file.write('First html file')
	file.close()
print('html file created')


