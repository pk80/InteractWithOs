#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], 'w') as file:
    lines = file.readlines()
    for line in lines:
        old = line.strip()
        new = old.replace('jane','jdoe')
        subprocess.run(['mv',old,new])
    file.close()

print('Finished change jane')
