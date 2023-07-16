import collections
from typing import OrderedDict 
dict=OrderedDict()
n=int(input())
for i in range(n):
    entry=input().split(' ')
    dict[entry[0]]=entry[1]
string=input().split(' ')
output=list()
for word in list(string):
    output.append(dict.get(word,word))
print(' '.join(output))
