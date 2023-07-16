import os
os.system('cls')  # on windows
string=input()
string=string.lower()
string=string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
newst=""
for letter in string:
     letter="."+letter
     newst+=letter
print(newst)