import os
os.system('cls')  # on windows
string=input()
count=0
for i in range(0,len(string)):
    if string[i].isupper():
        count+=1
if count> (len(string)-count):
    string=string.upper()
else:
    string=string.lower()
print(string)