from bs4 import BeautifulSoup as bs4
import re
import requests
import mysql.connector
site="https://www.mitacs.ca/en/programs/accelerate/open-projects?field_title_value=&field_project_type_value_i18n=All&field_location_s_where_project_c_country=CA&field_location_s_where_project_c_administrative_area=All&field_location_s_where_project_c_locality=&field_desired_education_level_value_i18n%5B0%5D=postdoc&page=1"
page=requests.get(address)
soup=bs4(page.content,'html.parser')
val=soup.find_all('h2', attrs={"class":"field-content title"})
count=0