# Input stream
#m.hosSein.python
#f.miNa.C
#m.aHMad.C++
#f.Sara.java

# Output stream
#f Mina C
#f Sara java
#m Ahmad C++
#m Hossein python
from typing import OrderedDict
# Input the string and seperate the information
# get the number of entries
n=int(input())
ID=OrderedDict()
# next lines include entries in form of gender.nonstandardName.programminglanguage
for j in range(n):
    field=input().split('.')
    field[1]= field[1].lower().capitalize()
    ID[j]=field
ID=sorted(ID.values(), key= lambda x: (x[0],x[1]))
for x in ID:
    print(x[0], x[1], x[2])

