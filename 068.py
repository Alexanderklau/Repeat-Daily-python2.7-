from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://www.bilibili.com/")
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1)
