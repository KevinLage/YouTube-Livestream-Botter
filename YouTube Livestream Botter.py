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

https://github.com/KevinLage/YouTube-Livestream-Botter
"""

print(intro)
if platform.system() == "Windows": #checking OS
    clear = "cls"
else:
    clear = "clear"

iPhone_UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1")

proxy_loading = input("[1] Load Proxys from APIs\n[2] Load Proxys from proxys.txt\n")

token = input("ID?\n")
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
    global proxy_loading
    def update(self):
        while True:

            if proxy_loading == "2":
                data = ''
                data = open("proxys.txt", "r").read()
                self.splited += data.split("\n") #scraping and splitting proxies
            else:
                data = ''
                urls = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt","https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes","https://www.proxy-list.download/api/v1/get?type=https&anon=elite"]
                for url in urls:
                    try:
                        data += requests.get(url).text
                        self.splited += data.split("\n")
                        self.splited = [s.replace('\r', "") for s in self.splited]
                    except:
                        print("Proxy loading failed!")
                        pass
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
            ua = random.choice(iPhone_UA)
            s = requests.session()
            random_proxy = proxy1.FormatProxy()

            resp = s.get("https://m.youtube.com/watch?v=" + token + "?disable_polymer=1",headers={'Host': 'm.youtube.com', 'Proxy-Connection': 'Keep-Alive', 'User-Agent': ua, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache'},proxies=random_proxy)   # simple get request to youtube for the base URL
            url = resp.text.split(r'videostatsWatchtimeUrl\":{\"baseUrl\":\"')[1].split(r'\"}')[0].replace(r"\\u0026",r"&").replace('%2C',",").replace("\/","/")  #getting the base url for parsing
            cl = url.split("cl=")[1].split("&")[0] #parsing some infos for the URL
            ei = url.split("ei=")[1].split("&")[0]
            of = url.split("of=")[1].split("&")[0]
            vm = url.split("vm=")[1].split("&")[0]
            s.get("https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=isWmmj2C9Y2vULKF&docid=" + token + "&ver=2&cmt=7334&ei=" + ei + "&fmt=133&fs=0&rt=1003&of=" + of +"&euri&lact=4418&live=dvr&cl=" + cl + "&state=playing&vm=" + vm + "&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=GB&rtn=1303&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1003&muted=0&st=7334&et=7634",headers={'Host': 's.youtube.com', 'Proxy-Connection': 'Keep-Alive', 'User-Agent': ua, 'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Referer': 'https://m.youtube.com/watch?v=' + token},proxies=random_proxy)   # API GET request

            a.botted += 1
        except:
            pass



maxthreads = int(input("How many Threads? Recommended: 500 - 1000\n"))

threading.Thread(target=a.printservice).start()
num = 0
while num < maxthreads :
    num += 1
    threading.Thread(target=bot).start()


threading.Thread(target=bot).start()
