import os
os.system('cls')  # on windows
name_array=list()
for i in range(1,11):
    name=input().lower()
    name=name.capitalize()
    name_array.append(name)
print(*name_array, sep="\n")
