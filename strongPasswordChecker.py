import re

strongPassword = re.compile(r'''
    ([a-z]+[A-Z]+[0-9]+|
    [a-z]+[0-9]+[A-Z]+|
    [A-Z]+[a-z]+[0-9]+|
    [A-Z]+[0-9]+[a-z]+|
    [0-9]+[a-z]+[A-Z]+|
    [0-9]+[A-Z]+[a-z]+)+
    ''', re.VERBOSE)


while True: 
    print('''Type your password here.
A strong password contains numbers, UPPERCASE and lowercase letters, and is at least 8 characters long.''')
    password = input()
    mo = strongPassword.search(password)
    if mo != None and len(password) >= 8:
        print('This password is strong.')
        break
    else:
        print('This password is weak.')
            
