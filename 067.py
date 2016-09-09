from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageurl):
    global pages
    html = urlopen("http://www.bilibili.com/" + pageurl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a",href = re.compile("^(/bili/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
    getLinks("")