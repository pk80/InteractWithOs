# Filtering Log files with regular expressions

import re

# logfile = sys.argv[1]
# logfile = input('Provide file information(path to file) : ')
logfile = '/Users/praveen/PycharmProjects/InteractWithOS/mylogs/syslog'
usernames = {}
# usernames = {}
# name = "good_user"
# usernames[name] = usernames.get(name, 0) + 1
# print(usernames)
# usernames[name] = usernames.get(name, 0) + 1
# print(usernames)

with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        # print(line.strip())
        # line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line.strip())
        # print(result[1])
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1

print(usernames)
