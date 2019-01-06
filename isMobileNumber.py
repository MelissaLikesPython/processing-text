# This program finds UK mobile number pattern in message
# written either only in numerics or with a space
# without using regular expressions.

message = '''Call me on 07800 123123 tomorrow. Or try 07899123123'''

def isMobileNumberNumeric(text):
    if len(text) != 11:
        return False
    for i in range(len(text)):
        if not text[i].isdecimal():
            return False       
    return True

def isMobileNumberWithSpace(text):
    if len(text) != 12:
        return False
    for i in range(len(text)):
        if not (text[0:5].isdecimal()
                and text[5].isspace()
                and text[6:13].isdecimal()):
            return False
    return True

def isMobileNumber(text):
    for i in range(len(text)):
        chunk = message[i:i+11]
        if isMobileNumberNumeric(chunk):
            print('Mobile number found: ' + chunk)
        elif not isMobileNumberNumeric(chunk):
            chunk2 = message[i:i+12]
            if isMobileNumberWithSpace(chunk2):
                print('Mobile number found: ' + chunk2)        
    print('Done')  

isMobileNumber(message)

