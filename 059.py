from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
def getTitle(url):
     try:
         html = urlopen(url)
     except HTTPError as e:
         return None
     try:
         bsObj = BeautifulSoup(html.read())
         model = bsObj.title
     except AttributeError as e:
         return None
     return model
model = getTitle("https://www.zhihu.com/",)
if model == None:
    print("Title could not be found")
else:
    print(model)
