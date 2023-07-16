from typing import OrderedDict
import random

class Human:
    count=0
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
class player(Human):
    def __init__(self, name,team):
        super().__init__(name)
        self.team=team
player_dic=OrderedDict()
player_list=input().split('-')
n=int(len(player_list)/2)
teams=['A']*n+['B']*n
random.shuffle(teams)
a=player('Hossein', 'A')
for i in range(len(player_list)):
    player_dic[i]=player(player_list[i],teams[i])
    Human.count+=1
for k in list(player_dic.keys()):
    print(player_dic[k].name, player_dic[k].team)
