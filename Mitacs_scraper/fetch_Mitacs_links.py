from bs4 import BeautifulSoup as bs4
import re
import requests
import mysql.connector
site="https://www.mitacs.ca/en/programs/accelerate/open-projects?field_title_value=&field_project_type_value_i18n=All&field_location_s_where_project_c_country=CA&field_location_s_where_project_c_administrative_area=All&field_location_s_where_project_c_locality=&field_desired_education_level_value_i18n%5B0%5D=postdoc&page=1"
page=requests.get(address)
soup=bs4(page.content,'html.parser')
cnx = mysql.connector.connect(user='root', password='*****', host='0.0.0.0', database='mydb')
link=soup.find_all(onclick=re.compile("location.href"))

count=0
cursor=cnx.cursor()
for item in link:
    temp='https://www.mitacs.ca'+re.split('\'*\'',item['onclick'])[1]
    count+=1
    cursor.execute('INSERT INTO links VALUES (%s);',(temp))
    cnx.commit()

# query='SELECT * FROM cars;'
# cursor.execute(query)
# for (t,p,m) in cursor:
#      print('%s %s %s' %(t,p,m))#
cursor.close()
cnx.close()