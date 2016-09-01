from urllib.request import urlopen
from bs4 import BeautifulSoup

textPage = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(textPage.read(),'utf-8')