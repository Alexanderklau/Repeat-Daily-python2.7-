import json
from urllib.request import urlopen
def getConutry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getConutry("50.78.253.58"))
