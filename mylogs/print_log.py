#!/usr/bin/env python3

import sys
import re

logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        # print(line.strip())
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line.strip())
        # print(result[1])
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1

print(usernames)
