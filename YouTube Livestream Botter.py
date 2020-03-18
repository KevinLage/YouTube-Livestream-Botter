import os
import random
import string
import threading
import time
from queue import Queue
import platform

import requests
from colorama import Fore, init

intro = """
███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗      ██████╗  ██████╗ ████████╗████████╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║      ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║█████╗██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔╝
╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║╚════╝██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║      ██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
"""

print(intro)

if platform.system() == "Windows": #checking OS
    clear = "cls"
else:
    clear = "clear"

def randomName(size=11, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))


token = input("ID?\n")
url= "https://m.youtube.com/watch?v=" + token
url2 = "https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=Syr16u8qwHnPkVqI&docid=" + token + "&ver=2&cmt=2094&ei=1EJtXou2C6eoxN8PpqqNqAg&fmt=133&fs=0&rt=1769&of=rkW8h_g-Pta1U6EIuWGdvw&euri&lact=7275&live=dvr&cl=300532980&state=playing&vm=CAEQABgEKhhJc0gwZ2w0QmFfbTBWSXlWNm9ITmRRPT06MkFOcHN5N0FhUWlHOHl5QkQySUF1OGt6amlZYjZwN3hzNzRXV3hhTEE4NDZVU1h2TTV3&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=IQ&rtn=2069&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1769&muted=0&st=2094&et=2394"
class main(object):
    def __init__(self):
        self.combolist = Queue()
        self.Writeing = Queue()
        self.printing = []
        self.botted = 0
        self.combolen = self.combolist.qsize()

    def printservice(self): #print screen
        while True:
            if True:
                os.system(clear)
                print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
                print(
                    Fore.LIGHTCYAN_EX + f"Botted:{self.botted}\n")
                for i in range(len(self.printing) - 10, len(self.printing)):
                    try:
                        print(self.printing[i])
                    except (ValueError, Exception):
                        pass
                time.sleep(0.5)
a = main()
class proxy():

    def update(self):
        while True:
            data = ''
            urls = ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes","https://www.proxy-list.download/api/v1/get?type=https&anon=elite"]
            for url in urls:
                data += requests.get(url).text
                
            self.splited += data.split("\r\n") #scraping and splitting proxies
            time.sleep(600)
    
    def get_proxy(self):
        random1 = random.choice(self.splited) #choose a random proxie
        return random1
    def FormatProxy(self):
	    proxyOutput = {'https' :'https://'+self.get_proxy()}
	    return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)

proxy1 = proxy()
def bot():
    while True:
        try:
            s = requests.session()

            resp = s.get("https://m.youtube.com/watch?v=" + token,headers={'Host': 'm.youtube.com', 'Proxy-Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate'},proxies=proxy1.FormatProxy())   # simple get request to youtube for the base URL
            url = resp.text.split(r'videostatsWatchtimeUrl\":{\"baseUrl\":\"')[1].split(r'\"}')[0].replace(r"\\u0026",r"&").replace('%2C',",").replace("\/","/")  #getting the base url for parsing
            cl = url.split("cl=")[1].split("&")[0] #parsing some infos for the URL 
            ei = url.split("ei=")[1].split("&")[0]
            of = url.split("of=")[1].split("&")[0]
            vm = url.split("vm=")[1].split("&")[0]
            s.get("https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=isWmmj2C9Y2vULKF&docid=" + token + "&ver=2&cmt=7334&ei=" + ei + "&fmt=133&fs=0&rt=1003&of=" + of +"&euri&lact=4418&live=dvr&cl=" + cl + "&state=playing&vm=" + vm + "&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=GB&rtn=1303&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1003&muted=0&st=7334&et=7634",headers={'Host': 's.youtube.com', 'Proxy-Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1', 'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Referer': 'https://m.youtube.com/watch?v=' + token},proxies=proxy1.FormatProxy())   # API GET request
            
            
            a.botted += 1
        except Exception as E:
            pass


time.sleep(7)
maxthreads = int(input("How many Threads? Recommended: 500 - 1000\n"))

threading.Thread(target=a.printservice).start()
num = 0
while num < maxthreads :
    num += 1
    threading.Thread(target=bot).start()


threading.Thread(target=bot).start()

