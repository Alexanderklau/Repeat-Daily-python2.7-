from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.cuit.edu.cn/")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img",{"src":re.compile("\.\.\/Images\/Slide/img.*\.jpg")})
for image in images:
    print(image["src"])

# print(bsObj.find("img",{"src":"Images/Slide/2016_09_07_13_27_20_2720.jpg"}))