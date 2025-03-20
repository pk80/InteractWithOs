#!/usr/bin/env python3

import re

print('Exercise 1:')

line_1 = "Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)"
line_2 = "May 27 11:45:40 ubuntu.local ticky: ERROR Error creating ticket [#1234] (username)"

# result_1 = re.search(r'ticky: INFO ([\w ]*) ', line_1)
# result_2 = re.search(r'ticky: ERROR ([\w ]*) ',line_2)
# print(result_1)
# print(result_2)

# user_pattern = r'\((.*)\)$'
pattern = r'\w+ .*:\s(INFO)|(ERROR)+\s.*\s\((.*)\)$'
result = re.search(pattern, line_1)
print(result.groups())
