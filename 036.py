from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,inclideUrl):
    internalLiks = []
    for link in bsObj.findAll("a",href = re.compile("^(/|.*"+inclideUrl+")")):
        if link.attrs['href'] not in internalLiks:
            internalLiks.append(link.attrs['href'])
    return internalLiks
def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a",
                              href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts
def getRandomExternaLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internaLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internaLinks[random.randint(0,
                                                               len(internaLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]
def followExternalOnly(startingSite):
    externalLink = getRandomExternaLink("http://oreilly.com")
    print("随机外链:"+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")



