from tkinter import END
ValidAge=range(10,91)
CandidateAge=int(input())
Oldest=CandidateAge
while CandidateAge !=-1 and CandidateAge in ValidAge:
    CandidateAge=int(input())
    if CandidateAge not in ValidAge:
        #print('Error: invalid entry')
        END
    elif CandidateAge >= Oldest:
        Oldest=CandidateAge
print(Oldest)
