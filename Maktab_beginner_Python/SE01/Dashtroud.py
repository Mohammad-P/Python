from tkinter import END
TotalWin=0
TotalScore=0  
ValidScore=[0,1,3]
for i in range(1,31):
    Score=int(input())
    if Score==3:
        TotalWin=TotalWin+1
    elif Score not in ValidScore:
        print('Error: invalid entry')
        END
    TotalScore=TotalScore+Score
print(TotalScore,TotalWin)
