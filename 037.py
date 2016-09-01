import json
from urllib.request import urlopen
def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    respostJson = json.load(response)
    return respostJson.get("country_code")
print(getCountry("20.68.253.58"))
