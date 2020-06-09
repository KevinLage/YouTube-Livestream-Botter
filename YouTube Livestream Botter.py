#/usr/bin/env python3                                                                                                                                      
# -*- coding: UTF-8 -*-                                                                                                                                    
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

 .::::::.   .,-::::: :::::::..    :::.     .        :   :::::::.   :::     :::::::.      ...   ::::::::::::
;;;`    ` ,;;;'````' ;;;;``;;;;   ;;`;;    ;;,.    ;;;   ;;;'';;'  ;;;      ;;;'';;'  .;;;;;;;.;;;;;;;;''''
'[==/[[[[,[[[         [[[,/[[['  ,[[ '[[,  [[[[, ,[[[[,  [[[__[[|. [[[      [[[__[[|.,[[     '[[,   [[     
  '''    $$$$         $$$$$$c   c$$$cc$$$c $$$$$$$$"$$$  $$"'"'Y$$ $$'      $$'"''Y$$$$$,     $$$   $$     
 88b    dP`88bo,__,o, 888b "88bo,888   888,888 Y88" 888o_88o,,od8Po88oo,.___88o,,od8P"888,_ _,88P   88,    
  "YMmMY"   "YUMMMMMP"MMMM   "W" YMM   ""` MMM  M'  "MMM""YUMMMP" ""YUMMM""YUMMMP"   "YMMMMMP"      MMM    
refactoring in progress by: scramblr (https://github.com/scramblr)    -   based on og version by DeBos.

"""                                                                                                                                                        
                                                                                                                                                           
print(intro)                                                                                                                                               
                                                                                                                                                           
if platform.system() == "Windows": #checking OS                                                                                                            
    clear = "cls"                                                                                                                                          
else:                                                                                                                                                      
    clear = "clear"                                                                                                                                        
                                                                                                                                                           
def randomName(size=11, chars=string.ascii_letters + string.digits):                                                                                       
    return ''.join(random.choice(chars) for i in range(size))                                                                                              
                                                                                                                                                           
def get_random_alphaNumeric_string(stringLength=16):                                                                                                       
    lettersAndDigits = string.ascii_letters + string.digits + "_" + "-"                                                                                    
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))                                                                         
                                                                                                                                                           
def get_random_alphaNumeric_only(stringLength=13):                                                                                                         
    lettersAndDigits = string.ascii_letters + string.digits                                                                                                
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))                                                                         
                                                                                                                                                           
                                                                                                                                                           
# Changes by scramblr                                                                                                                                      
# These changes are to avoid fingerprinting this wonderful beast. Currently, it relies on too many static variables. And static variables are fingerprints.                                                                                                                                                           
# Lets shake it up. Also, we upgraded our iPhones to a newer iOS and became US viewers, as they are apparently worth more to Google or whatever. *shrug*   
# I know, I know.. it's just a template call, but we're up against Google here. Eventually they're gonna figure this shit out, let's start planning ahead now.                                                                                                                                                        
# Enjoy.                                                                                                                                                   
                                                                                                                                                           
cpnrandom = get_random_alphaNumeric_string(16)        # random cpn value, typically 16 in len. includes alpha-upper, alpha-lower, numeric, and -'s and _'s 
eirandom = get_random_alphaNumeric_only(13)           # ei value, typically 13 in len. includes alpha-upper, alpha-lower, numeric.                         
ofrandom = get_random_alphaNumeric_only(22)           # of value, typically 22 in len. includes alpha-upper, alpha-lower, numeric, and -'s and _'s         
vmrandom = get_random_alphaNumeric_only(112)          # vm value, typically 112 in len. includes alpha-upper, alpha-lower, numeric.                        
                                                                                                                                                           
                                                                                                                                                           
# Comment the lines below to stop debugging. We're geeks, so it's not a fuckin problem.                                                                                                                      
                                                                                                                                                           
print("Our new 'cpn' value: ",cpnrandom," ...Let's hope its not fucked up!")    # We're gonna generate random cpn's from now on. Google doesn't validate this.                                                                                                                                                        
print("Our new 'ei' value: ",eirandom," ...Let's hope its not fucked up!")      # We're gonna generate random ei's from now on, too. Again, Google doesn't validate this.                                                                                                                                             
print("Our new 'of' value: ",ofrandom," ...Let's hope its not fucked up!")      # We're gonna generate random of's from now on. Google dont validate these bitches.                                                                                                                                                   
print("Our new 'vm' value: ",vmrandom," ...Let's hope its not fucked up!")      # We're gonna generate random vm's from now on. Google aint got no time for validatin'!                                                                                                                                               
                                                                                                                                                           
                                                                                                                                                           
token = input("YouTube ID? (after the watch?v= part, dumbass.)\n")                                                                                                                                     
url = "https://m.youtube.com/watch?v=" + token  # Fixed some syntax stuff here. Nbd.                                                                       
url2 = "https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=" + cpnrandom + "&docid=" + token + "&ver=2&cmt=2094&ei=" + eirandom + "&fmt=133&fs=0&rt=1769&of=" + ofrandom + "&euri&lact=7275&live=dvr&cl=300532980&state=playing&vm=" + vmrandom + "&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=en_US&cr=IQ&rtn=2069&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1769&muted=0&st=2094&et=2394"                                                                                            
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
                    Fore.LIGHTCYAN_EX + f"ViewBot Sent To Proxy. Hope it hatches into a real viewer!:{self.botted}\n")    # Changed this because this only counts successful 200s, including 200s telling us to get fucked from the proxy.                                                                            
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
            url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=5000&anonymity=elite&ssl=yes"    # made this anonymous/elite only. Can expand to HTTP as well.                                                
            r = requests.get(url)                                                                                                                          
                                                                                                                                                           
            self.splited = r.text.split("\r\n") #scraping and splitting proxies                                                                            
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
            of = url.split("of=")[1].split("&")[0] # Leaving these alone since they're coming direct from Google. -scramblr                                
            vm = url.split("vm=")[1].split("&")[0]                                                                                                         
                                                                                                                                                           
#    Broke this out so we can learn while we game tha system.                                                                                              
#    This part of the HTTPS request is where we make a web call as an iPhone, and grab *real* values, instead of our bullshit from above. But, we will use our                                                                                                                                                        
#    bullshit to kick things off so that Google doesn't just block all API calls with *that one specific cpn value*. Same goes for them all.               
                                                                                                                                                           
            s.get("https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=" + cpnrandom + "&docid=" + token + "&ver=2&cmt=7334&ei=" + ei + "&fmt=133&fs=0&rt=1003&of=" + of + "&euri&lact=4418&live=dvr&cl=" + cl + "&state=playing&vm=" + vm + "&volume=100&c=MWEB&cver=2.20200529.03.00-new_canary_live&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=13.1.15E148&cmodel=iphone&cos=iPhone&cosver=13_4_1&cplatform=MOBILE&delay=5&hl=en_US&cr=US&rtn=1303&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1003&muted=0&st=7334&et=7634",headers={'Host': 's.youtube.com', 'Proxy-Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) GSA/36.0.169645775 Mobile/17E262 Safari/604.1', 'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5', 'Accept-Language': 'en-US,en;q=0.8,en-US;q=0.5,en;q=0.3', 'Referer': 'https://m.youtube.com/watch?v=' + token},proxies=proxy1.FormatProxy())   # API GET request                                                                                
                                                                                                                                                           
                                                                                                                                                           
            a.botted += 1                                                                                                                                  
        except Exception as E:                                                                                                                             
            pass                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
time.sleep(7)                                                                                                                                              
maxthreads = int(input("How many Threads? Recommended: 200 - Up to 1000 depending on CPU/RAM.\n"))                                                                                     
                                                                                                                                                           
threading.Thread(target=a.printservice).start()                                                                                                            
num = 0                                                                                                                                                    
while num < maxthreads :                                                                                                                                   
    num += 1                                                                                                                                               
    threading.Thread(target=bot).start()                                                                                                                   
                                                                                                                                                           
                                                                                                                                                           
threading.Thread(target=bot).start()                                                                                                                       
                                     
