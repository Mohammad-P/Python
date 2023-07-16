import os
os.system('cls')  # on windows
string=input().lower()
flipped=string[ ::-1]
if string==flipped:
    print('palindrome')
else:
    print('not palindrome')