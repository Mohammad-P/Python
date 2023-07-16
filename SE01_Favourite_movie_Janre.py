from operator import getitem, itemgetter
from typing import OrderedDict
Janre=dict()
n=int(input())
names=list()
Janre={'Action':0,'Comedy':0, 'Horror':0, 'Romance':0, 'History':0 , 'Adventure':0}
for i in range(n):
    row=input().split(' ')
    row.pop(0)
    names.extend(row)
for name in names:
    Janre[name]=Janre.get(name,0)+1
Janre=sorted(Janre.items(), key= lambda x: (-x[1], x[0]),reverse=False)
for k,v in Janre:
    print(k,':',v)
