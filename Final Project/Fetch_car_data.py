# The file recieves the manufacturere's name then update the site address of www.cars.com to
# search the used cars in US
# the items will be passed to " mydb.cars" table.
from bs4 import BeautifulSoup as bs4
import json
import re
import requests
import mysql.connector
cnx = mysql.connector.connect(user='root', password='123456789', host='127.0.0.1', database='mydb')
#make=input('Please input the manufacturere\'s name:').strip().lower()
p=1
while p <= 1000:
    site='https://www.cars.com/shopping/results/?page=1&page_size=10&dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=&maximum_distance=all&mileage_max=&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip='
    pageNum='page='+str(p)
    #print(p)
    address=re.sub(r'page=1',pageNum,site)
    page=requests.get(address)
    soup=bs4(page.content,'html.parser')
    val=soup.find_all('div',attrs={'class':'sds-page-section listings-page'})
    sec=val[0]
    goal=sec['data-site-activity']
    se=re.search(r'"vehicleArray":(\[.*}\])',goal)
    array=se.group(1).strip()
    results = []
    s_ = ' '.join(array[1:-1].split('\n')).strip()
    exp = re.compile(r'(\{.*?\})')
    for i in exp.findall(s_):
        try:
            results.append(json.loads(i))        
        except json.JSONDecodeError:
            pass    
    #values=[list(x.values()) for x in results]
    columns=[list(x.keys()) for x in results][0]
    #values_str=''
    ind=[22,1,7,8,10,11,12,15,21,23]
    columns=[columns[x] for x in ind]
    table_name = "cars"
    #sql_string="ALTER TABLE `mydb`.`cars` ADD UNIQUE INDEX `listing_id_UNIQUE` (`listing_id` ASC);"
    cursor=cnx.cursor()
    placeholder=', '.join(['%s']*len(results))
    for dic in results:
            val_pass=list()
            for c in columns:
               #str_value='\''+dic[c]+'\''
                   val_pass.append(dic[c])
               #print(c, val_pass)
            sql_string = "INSERT IGNORE INTO %s (%s) VALUES (%s)" % (table_name,', '.join(columns), placeholder)
                #print(sql_string)
            cursor.execute(sql_string,val_pass)
            cnx.commit()
    p+=1
#cursor.execute("SELECT exterior_color, COALESCE(exterior_color,'black') as exterior_color FROM mydb.cars;")
#cursor = cnx.cursor(buffered=True,dictionary=True)
#cursor.execute("SELECT fuel_type, ifnull(fuel_type,'Gasoline') as fuel_type FROM mydb.cars;")
#cnx.commit()
cursor.close()
cnx.close()
