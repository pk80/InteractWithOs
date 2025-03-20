#!/usr/bin/env python3

import re
import sys
import operator

error_messages = {}
user_entries = {}

with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        match = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)

        if match is None:
            continue

        code, err_msg, user = match.group(1), match.group(2), match.group(3)

        if err_msg not in error_messages.keys():
            error_messages[err_msg] = 1
        else:
            error_messages[err_msg] += 1

        if user not in user_entries.keys():
            user_entries[user] = {}
            user_entries[user]['INFO'] = 0
            user_entries[user]['ERROR'] = 0

        if code == 'INFO':
            user_entries[user]['INFO'] += 1
        elif code == 'ERROR':
            user_entries[user]['ERROR'] += 1

    file.close()

errors_list = sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)
users_list = sorted(user_entries.items(), key=operator.itemgetter(0))

errors_list.insert(0, ('Error', 'Count'))
# user_entries.insert(0, ('User', 'Info' 'Error')) # TypeError

with open('user_statistics.csv', 'w', newline='') as file:
    for key, value in users_list:
        file.write(str(key) + ',' + str(value['INFO']) + ',' + str(value['ERROR']) + '\n')
    file.close()

with open('error_message.csv', 'w', newline='') as file:
    for key, value in errors_list:
        file.write(str(key) + ',' + str(value) + '\n')
    file.close()

print('completed ticky check')
