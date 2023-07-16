import re
def user_length_check(string):
    if username==[] or len(username)<= 7:
        Valid=False
        return Valid
    else:
        Valid=True
        
        return Valid
regex_email = r'[A-Za-z0-9_][^@%$#!~*&-]+@[A-Za-z0-9]+\.[A-Za-z]'
Valid=False
Flag=False
username=input()
if not user_length_check(username):
    Valid=False
else:
    Valid=True
if Valid:
    if not re.search(regex_email,username):
        Flag=False
    else:
        Flag=True
else:
    Flag=False
if Flag:
    print('OK')
else:
    print ('WRONG')
