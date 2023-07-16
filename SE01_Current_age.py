# this code estimates the age of the user
from datetime import date, datetime
import time
Flag=True
strdate=input().split('/')
intdate=list(map(int,strdate))
yyyy=intdate[0]
if intdate[1] in range(13):
    mm=intdate[1]
else:
    Flag=False
if intdate[2] in range(32):
    dd=intdate[2]
else:
    Flag=False
if Flag==True:
    inputDate='-'.join(strdate)
    Birth_date=datetime.fromisoformat(inputDate)
    today = date.today()
    year_difference=today.year-Birth_date.year-((today.month,today.day)<(Birth_date.month,Birth_date.day))
    #date_to_now=abs(year_difference)
    print(year_difference)
else:
    print('WRONG')


