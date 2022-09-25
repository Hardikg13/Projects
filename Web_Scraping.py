# pip install bs4
# pip install requests
# pip3 install lxml ( To get a parser)

import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
title = soup.find_all('h2',{'class':'post-title'})
for t in title:
    print(t.getText())