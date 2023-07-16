#ایران – اسپانیا
#ایران – پرتغال
#ایران – مراکش
#اسپانیا – پرتغال
#اسپانیا – مراکش
#پرتغال - مراکش
# __________ reults_________________
#2-2    Iran-Spain
#2-1    Iran-Portugal
#1-2    Iran-Morocco
#2-2    Spain-Portugal
#3-1    Spain-Morocco
#2-1    Portugal-Morocco
from typing import OrderedDict


class team:
    def __init__(self, name):
        self.name=name
        self.wins=self.loses=self.draws=self.goal_difference=0
        self.points=0
# updating function         
def scoree(A,B,a,b):
    if a==b:
        A.draws=A.draws+1
        B.draws=B.draws+1
        A.points=3*A.wins+A.draws
        B.points=3*B.wins+B.draws
    elif a>b:
        A.wins= A.wins+1
        A.goal_difference=A.goal_difference+ abs(a-b)
        A.points=3*A.wins+A.draws
        # team B
        B.loses= B.loses+1
        B.goal_difference=B.goal_difference-abs(a-b)
        B.points=3*B.wins+B.draws
    elif a<b:
        B.wins= B.wins+1
        B.goal_difference=B.goal_difference+ abs(a-b)
        B.points=3*B.wins+B.draws
        # team A
        A.loses= A.loses+1
        A.goal_difference=A.goal_difference-abs(a-b)
        A.points=3*A.wins+A.draws

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

ResultTuples=list()
# Team A - team B match
teamA=team('Iran')
teamB=team('Spain')
teamC=team('Portugal')
teamD=team('Morocco')
for i in range (6):
    p=map(int,input().split('-'))
    scores=tuple(p)
    if i==0:
        scoree(teamA,teamB,scores[0],scores[1])
    if i==1:
        scoree(teamA,teamC,scores[0],scores[1])
    elif i==2:
        scoree(teamA,teamD,scores[0],scores[1])
    elif i==3:
        scoree(teamB,teamC,scores[0],scores[1])
    elif i==4:
        scoree(teamB,teamD,scores[0],scores[1])
    elif i==5:
        scoree(teamC,teamD,scores[0],scores[1])       
#     ResultTuples.append(tuple(p))
# print(ResultTuples)
#ResultTuples=[(2, 2), (2, 1), (1, 2), (2, 2), (3, 1), (2, 1)] # first section output


Table=[teamA, teamB, teamC, teamD]
table=sorted(Table,key=lambda x: (-x.points, -x.wins, x.name), reverse=False)

for object in table:
     print('{o.name}  wins:{o.wins} , loses:{o.loses} , draws:{o.draws} , goal difference:{o.goal_difference} , points:{o.points}'. format(o=object))