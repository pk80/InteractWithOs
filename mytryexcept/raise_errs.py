#!/usr/bin/env python3
from unicodedata import digit


def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True


print(validate_user("", 1))  # False
# print(validate_user("", -1)) # ValueError
print(validate_user("myuser", 1))  # True
print(validate_user("88", 1))  # True
# print(validate_user(88, 1)) # AssertionError
# print(validate_user([], 1))  # AssertionError
# print(validate_user(['name'], 1))  # AssertionError
# print(validate_user([3], 1))  # AssertionError
