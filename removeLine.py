# This program removes a recurring newline phrase from corpus of text.

myText = '''I think we should meet at 8pm. You can shop before and
pick up the shoes you need, without anyone having to hang around
while you try them on.

Save Copy Delete

Why don't we meet earlier so we can grab a beer before eating?

Save Copy Delete

Okay if you'll be done by then what about 7?

Save Copy Delete

Ok I'll text you a place to meet.

Save Copy Delete'''


def deleteLine(withLine):

    lines = withLine.split('\n') # Splits the text at each newline.

    while True: # Deletes recurring phrase. 
        if 'Save Copy Delete' in lines:
            lines.remove('Save Copy Delete')
        if 'Save Copy Delete' not in lines:
            break

    lines = '\n'.join(lines) # Recreates the text without the phrase.     
    print(lines)

deleteLine(myText)    

    
    
