import os
os.system('cls')  # on windows
string=input()
stripped=string.replace('+',"")
#print(stripped)
sortchar=sorted(stripped)
#print(sortchar)
sortcharwithplus=[x.replace(x,'+'+x) for x in sortchar]
#print(sortcharwithplus)
string="".join(sortcharwithplus)
string=string[1:]
print(string)