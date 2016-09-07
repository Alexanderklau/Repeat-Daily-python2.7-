from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.cuit.edu.cn/")
bsObj = BeautifulSoup(html)
namelist = bsObj.findAll("head")
for name in namelist:
    print(name.get_text())
# for sibling in bsObj.find("table").tr.next_sibling:
#     print(sibling)