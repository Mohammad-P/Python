import os
os.system('cls')  # on windows
string=input()
if string.find('AB') !=-1:
    updated=string.replace('AB','ss')
    if updated.find('BA') !=-1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')