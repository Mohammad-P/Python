import os
os.system('cls')  # on windows
n=int(input())
rep=input().split(" ")
count=0
team=sum([int(item) for item in rep if int(item)<4])//3
print(team)



