import requests
import json
import re
def parse_text(text):
    pattern = r"/\w+"
    crypto = re.search(pattern, text).group()
    return crypto[1:]
def get_data(obl):
    returnString = "Akert is now"
    found = False
    url = ('http://ubilling.net.ua/aerialalerts/')
    request = requests.get(url).json()
    states = request["states"]
    for key, value in states.items():
            if(obl in key):
                if(value["alertnow"] == False):
                    returnString = "No alert"
                    found = True
                returnString +="\n Last alert" + value["changed"] ;
    if not found:
        return 'Type correct (Вінницька область)'
    return returnString

def intmain():
    print(parse_text('Zr nfv e /Київська'))

if __name__ == '__main__':
    intmain()
