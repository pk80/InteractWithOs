#!/usr/bin/env python3

import re

errs_dict = {}
user_count = {}

filename = 'syslog.log'
with open(filename, 'r') as file:
    logs = file.readlines()
    for log in logs:
        info_pattern = r'\w+ .*:\s(INFO)|(ERROR)+\s.*\s\((.*)\)$'
        result = re.search(info_pattern, log)
        if result is None:
            continue
        if result[3] is not None:
            user_count[result[3]] = user_count.get(result[3], 0) + 1


print(user_count)