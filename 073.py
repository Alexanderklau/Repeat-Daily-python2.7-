import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://www.bilibili.com/"

def getAbsoluteURL(baseUrl,source):
    if source.startwith("http://www."):
        url = "http://" + source[11:]
    elif source.startwith("http://"):
        url = source
    elif source.startwith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url
def getDownloadPath(baseUrl,abslouteUrl,downloadDirectory):
    path = abslouteUrl.replace("www.","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
        return path
    html = urlopen("http://www.bilibili.com/")
    bsObj = BeautifulSoup(html)
    downloadList = bsObj.findAll(src = True)

    for download in downloadList:
        fileUrl = getAbsoluteURL(baseUrl,download["src"])
        if fileUrl is not None:
            print(fileUrl)
    urlretrieve(fileUrl,getAbsoluteURL(baseUrl,fireUrl,downloadDirectory))
