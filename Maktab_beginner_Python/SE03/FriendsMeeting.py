X=input().split(" ")
num_list=[int(item) for item in X]
num_list.sort()
Min=num_list[2]-num_list[0]
print(Min)