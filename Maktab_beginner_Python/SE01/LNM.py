Num_length=10
num_array=list()
num_count=list()
MaxCount=1
MaxNum=list()
def TMM(num):
    count=0
    for j in range(1,num+1):
        if num % j==0:
            count=count+1
    return count
for i in range(0,Num_length):
    Number=int(input())
    num_array.append(Number)
    Dcount=TMM(Number)
    num_count.append(Dcount)
    if Dcount >= MaxCount:
        MaxCount=Dcount
for i in range(0,Num_length):
    if num_count[i]>=MaxCount:
        MaxNum.append(num_array[i])
MaxNum=sorted(MaxNum, reverse=True)
print(MaxNum[0],MaxCount)
#print(num_array)
#print(num_count)
