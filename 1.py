from urllib import request
from bs4 import BeautifulSoup
import re
webPage=request.urlopen('https://www.zhihu.com/question/38478558').read()

file=open('webPage.html','wb')
file.write(webPage)
file.close()

soup=BeautifulSoup(webPage,'html5lib')
for link in soup.find_all('img'):
    print(link.get('data-actualsrc'))

print(soup.getText())