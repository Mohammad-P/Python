import collections
from typing import OrderedDict
n=int(input())
roster=list()
for i in range(n):
    name=input()
    roster.append(name)
roster.sort()
counter=OrderedDict()
for name in roster:
    counter[name]=counter.get(name,0)+1
for name in list(counter.keys()):
    print(name, counter[name])
