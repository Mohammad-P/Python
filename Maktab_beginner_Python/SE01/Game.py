# This program executes "Guess the number" game between the PC and User
#
import random
from turtle import Screen
UpMargin=99   # Initial value of Guess range
LowMargin=1
count=0
InitialGuess=random.randint(LowMargin,UpMargin-1)
print(InitialGuess)
Eval=input()
#print('Your evaluation is:',Eval)
while True:
    if Eval=='d':
        print('Your number',InitialGuess, 'has been found after',count,'try')
        break
    elif Eval=='b':
      #  print('Shrinking the boundaries')
        LowMargin=InitialGuess
    elif Eval=='k':
     #   print('Enlarging the boundaries')
        UpMargin=InitialGuess
    else:
        print('You enteres a wrong character')
        break
   # print(count,LowMargin,UpMargin)
    InitialGuess=random.randint(LowMargin,UpMargin)
  #  print('My new number is',InitialGuess)
    print(InitialGuess)
    Eval=input()
   # print('Your evaluation is:',Eval)

    count +=1
print('Game Over')