import re
from urllib import request
webPage=request.urlopen('https://www.zhihu.com/question/38478558').read()
search=re.compile(r'(?<=question/).*?(?=" data-id=)')
for item in search.findall(str(webPage)):
    if len(item)==8:
        print(item)
