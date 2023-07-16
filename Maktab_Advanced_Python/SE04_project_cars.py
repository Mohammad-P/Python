# The file recieves the manufacturere's name then update the site address of www.cars.com to
# search the used cars in US
# the first twenty items will be passed to " mydb.cars" table.
from bs4 import BeautifulSoup as bs4
import re
import requests
import mysql.connector
make=input('Please input the manufacturere\'s name:').strip().lower()
site='https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=honda&maximum_distance=all&mileage_max=&page_size=20&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip='
address=re.sub(r'honda',make,site)
page=requests.get(address)
soup=bs4(page.content,'html.parser')
val=soup.find_all("span",attrs={"class":"primary-price"})
cnx = mysql.connector.connect(user='root', password='***********', host='0.0.0.0', database='mydb')
#print('Connected')
count=0
cursor=cnx.cursor()
for item in val:
    count+=1
    price=item.text
    mileage=item.parent.parent.find('div','mileage').text
    title=item.parent.parent.find('h2','title').text
    if count < 21:
        cursor.execute('INSERT INTO cars VALUES (%s,%s,%s);',(title,price,mileage))
        cnx.commit()
cursor.close()
cnx.close()
