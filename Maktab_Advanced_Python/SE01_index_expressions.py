
from typing import Counter, ItemsView, OrderedDict

text=OrderedDict()
endwithdot=list()
endwithcomma=list()
count=1
context=input().split(' ')
for i in range(len(context)):
    if context[i][-1]=='.':
        context[i]=context[i][:-1]
        endwithdot.append(count)
    if context[i][-1]==',':
        context[i]=context[i][:-1]
        endwithcomma.append(count)
    text[count]=context[i]
    count+=1
values=[v for k,v in text.items() if v.istitle() or v.isupper()]
#for word in values:
endwithdot.pop()
endwithdot.append(0)
wordsafterdot=[text.__delitem__(i+1) for i in endwithdot]
# To repel the capitalized word in the beginning of the sentences
output=list()
for k , v in text.items():
    if v in values:# and v not in wordsafterdot:
         output.append(k)  
            #    print(k)
if output==[]:
    print('None')
for i in output:
    print('{}:{}' .format(i,text.get(i)))

#print('________________________________________________')
#print(endwithcomma)