from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.bilibili.com/")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img",{"src":re.compile("jpg*")})
for image in images:
    print(images["src"])