# This program finds UK mobile number pattern in message
# written either only in numerics or with a space
# using a regular expression.

import re

message = '''Please give me a call asap at 07890123999
or 07899123123 during normal working hours.'''

def mobileNumberFinder(text):
    phoneNumRegex = re.compile(r'\d\d\d\d\d\s*\d\d\d\s*\d\d\d')
    print('Mobile numbers found: ' + ', '.join(phoneNumRegex.findall(message)))
    
mobileNumberFinder(message)
