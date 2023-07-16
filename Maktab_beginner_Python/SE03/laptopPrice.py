import os
from tkinter.tix import COLUMN
os.system('cls')  # on windows
n=int(input())
lap=[]
Q=list()
P=list()
ind=list()
found=0
for i in range(n):
    row=input().split(" ")
    P.append(row[0])
    Q.append(row[1])
P=[int(item) for item in P]
Q=[int(item) for item in Q]
#
for i in range(n):
    count=0
    for j in range(0,i+1):
        count+=1
        if P[i]< P[j]:
            if Q[i]>Q[j]:
                found=1
    count=i
    for j in range(i,len(P)):
        count+=1
        if P[i]< P[j]:
            if P[i]< P[j]:
                if Q[i]>Q[j]:
                 found=1
if found ==1:
    print('happy irsa')
else:
    print('poor irsa')    
