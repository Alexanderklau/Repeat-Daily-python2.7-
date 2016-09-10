from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).finaAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl + "&action=history"
    print("history url is:"+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipAddresses = bsObj.findAll("a",{"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
        return addressList
    links = getLinks("/wiki/Python_(programming_language")
    while(len(links) > 0):
        for link in links:
            print("----------------------")
            historyIPs = getHistoryIPs(link.attrs)