Num=int(input())
for den in range(2,Num):
    if Num % den==0:
        print('not prime')
        break
    elif den==Num-1:
        print('prime')
       