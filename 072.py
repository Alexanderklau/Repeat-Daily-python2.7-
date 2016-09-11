from urllib.request import urlretrieve
from urllib.request import urlopen
import os
from bs4 import BeautifulSoup

html = urlopen("http://www.bilibili.com/")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a",{"id":"logo"}).find("png")["src"]
urlretrieve(imageLocation,"logo.png")
