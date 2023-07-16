import collections
from typing import OrderedDict 
dict=OrderedDict()
n=int(input())

# function to return key for any value
def get_key(val):
    for key, value in dict.items():
         if val == value:
             return key
#main program
for i in range(n):
    entry=input().split(' ')
    dict[entry[0]]=[entry[1], entry[2], entry[3]]
string=input().split(' ')
output=list()
En=OrderedDict()
Ge=OrderedDict()
Sp=OrderedDict()
for i in dict:
    for d in dict[i]:
        En[d]=i
for word in string:
    output.append(En.get(word,word))
print(' '.join(output))