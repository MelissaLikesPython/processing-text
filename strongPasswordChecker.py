# Detects if a password string is strong.

import re

print('Type your password here.')

password = input()

strongPassword = re.compile(r'''
    ([a-z]+[A-Z]+[0-9]+|
    [a-z]+[0-9]+[A-Z]+|
    [A-Z]+[a-z]+[0-9]+|
    [A-Z]+[0-9]+[a-z]+|
    [0-9]+[a-z]+[A-Z]+|
    [0-9]+[A-Z]+[a-z]+)+
    ''', re.VERBOSE)

mo = strongPassword.search(password)

if mo != None and len(password) >= 8:
    print('This password is strong.')
else:
    print('This password is weak.')
            


