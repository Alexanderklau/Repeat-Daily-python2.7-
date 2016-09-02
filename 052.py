from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def cleanInput(input):
    input = re.sub('\n+'," ",input)
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +'," ",input)
    input = bytes(input,'utf8')
    input = input.decode("ascii","ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
        return cleanInput
def narms(input,n):
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

