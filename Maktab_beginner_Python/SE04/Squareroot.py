import math
n=int(input())
num_array=list()
for num in range(n):
    entry=int(input())
    entry=math.sqrt(entry)
    s = '{:.8f}'.format(entry)
    #print(s)
    num_array.append(s)
#print(num_array)    
for num in (num_array):
    num=num[:-4]
    print(num)
