import urllib.request
url = "http://www.cuit.edu.cn/"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
print(data)