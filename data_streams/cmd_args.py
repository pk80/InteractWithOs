#!/usr/bin/env python3
import os.path
import sys

print(sys.argv)

# % wc cmd_args.py
#        7       5      54 cmd_args.py
# % echo $?
# 0
# % wc unknown.py
# wc: unknown.py: open: No such file or directory
# % echo $?
# 1

filename = sys.argv[1]
if not os.path.exists(filename):
    with open(filename,'w') as file:
        file.write('new file created\n')
else:
    print(f'Error: the file {filename} already exists!')
    sys.exit(1)

# % ./cmd_args.py newfile
# ['./cmd_args.py', 'newfile']
# % ./cmd_args.py newfile
# ['./cmd_args.py', 'newfile']
# Error: the file newfile already exists!
# $ echo $?
# 1
