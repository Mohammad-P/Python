from bs4 import BeautifulSoup as bs4
import requests

page=requests.get('https://divar.ir/s/tehran')
soup=bs4(page.content,'html.parser')
s="kt-post-card__body"
val=soup.find_all("div",attrs={"class":s})
keyword='توافقی'
for ads in val:
    if keyword in ads.get_text():
        print(ads)