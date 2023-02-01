from json import loads , load , dumps
from subprocess import Popen , PIPE
from platform import system as iden
from bs4 import BeautifulSoup
from datetime import date
from colorama import Fore
from time import strftime
from random import choice
from requests import get
from os.path import isfile
from os import system
from sys import argv
from re import *
w = Fore.WHITE
red = Fore.RED
b = Fore.BLUE
g = Fore.GREEN
c = Fore.CYAN
if iden() != "Windows":
 from readline import parse_and_bind
 parse_and_bind('tab:complete')
def banner():
    if iden() == 'Windows':
        banner_Windows()
    else:system('clear ; python3 banner.py')
def banner_Windows():
    system('cls')
    colors = [w , red , b , g , c]
    print (f'''{choice(colors)}
    
                     _           _____ _    
                    | |         |  _  | |   
                    | |__   ___ | | | | | __
                    | '_ \ / _ \| | | | |/ /
                    | | | | (_) \ \_/ /   < 
                    |_| |_|\___/ \___/|_|\_\ V 1.0
                        
                        Coded BY : Ali Mansour


    ''')
def del_repeat( name ):
    for name_ in name:
        with open(name_ , 'r')as f:
            data = set(f.readlines())
            fx = open(name_ , 'w')
            for line in data :
                fx.write(line.rstrip() + '\n')
            fx.close()
def sub_collector(target):
    doms = open(f"{target}-subdomains.txt" , 'a')
    try:
        print (f'{w}[{red}+{w}] {g}[{strftime("%H:%M:%S")}] {g} Start .')
        print (f"{w}[{b}*{w}] {c}subdomainfinder.c99")
        print (f"{w}[{b}*{w}] {c}otx.alienvault")
        print (f"{w}[{b}*{w}] {c}securitytrails")
        print (f"{w}[{b}*{w}] {c}hackertarget")
        print (f"{w}[{b}*{w}] {c}rapiddns.io")
        print (f"{w}[{b}*{w}] {c}virustotal")
        print (f"{w}[{b}*{w}] {c}riddler.io")
        print (f"{w}[{b}*{w}] {c}urlscan")
        print (f"{w}[{b}*{w}] {c}jldc.me")
        print (f"{w}[{b}*{w}] {c}censys")
        print (f"{w}[{b}*{w}] {c}crt.sh{w}")
        nn = 0
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}
        for month in range(6 , 13):
            for i in range(1 , 31):
                if nn != 0:
                    break
                my_date = date(date.today().year - 1 , month , i)
                html_doc_1 = get(f"https://subdomainfinder.c99.nl/scans/{my_date}/{target}" ,allow_redirects=True , headers=headers)
                if not "Something went wrong while scanning" in html_doc_1.text:
                    soup = BeautifulSoup(html_doc_1.text, 'html.parser')
                    for sub in soup.find_all("a"):
                        if sub.get("href"):
                            if target in sub.get("href") and "subdomainfinder.c99.nl/scans" not in sub.get("href"):
                                print (sub.get("href")[2:])
                                doms.write(sub.get("href")[2:] + '\n')
                                nn += 1
                    print (f"{w}[{b}*{w}] Reference: {html_doc_1.url}")
            if nn != 0:
                break
        for n in range(1 , 101):
            html_doc_2 = get(f"https://rapiddns.io/subdomain/{target}?page={str(n)}#result" , allow_redirects=True , headers=headers)
            soup = BeautifulSoup(html_doc_2.text, 'html.parser')
            for sub in soup.find_all("td"):
                if sub.text.endswith(target):
                    print (sub.text)
                    for sub_ in sub.text.split('\n'):
                     doms.write(sub_ + '\n')
        req = get(f"https://api.securitytrails.com/v1/domain/{target}/subdomains?apikey=lEDJ6fVras9R8doewLFuJ6WnV0gumSR6").text
        for sub in loads(req)["subdomains"]:
            print (sub + '.' + target)
            doms.write(sub + '.' + target + '\n')
        req = get(f"https://jldc.me/anubis/subdomains/{target}" , headers=headers).text
        for sub in loads(req):
            print (sub)
            doms.write(sub + '\n')
        # Developed By Me This Function Coded In AORT Tool from the next code except virustotal depart
        r = get("https://crt.sh/?q=" + target + "&output=json", timeout=20)
        f_json = dumps(loads(r.text), indent=4)
        crt_domains = sorted(set(findall(r'"common_name": "(.*?)"', f_json)))
        for dom in crt_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = get(f"https://otx.alienvault.com/api/v1/indicators/domain/{target}/passive_dns", timeout=20)
        alienvault_domains = sorted(set(findall(r'"hostname": "(.*?)"', r.text)))
        for dom in alienvault_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = get(f"https://api.hackertarget.com/hostsearch/?q={target}", timeout=20)
        hackertarget_domains = findall(r'(.*?),', r.text)
        for dom in hackertarget_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = get(f"https://riddler.io/search/exportcsv?q=pld:{target}", timeout=20)
        riddler_domains = findall(r'\[.*?\]",.*?,(.*?),\[', r.text)
        for dom in riddler_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = get(f"https://urlscan.io/api/v1/search/?q={target}", timeout=20)
        urlscan_domains = sorted(set(findall(r'https://(.*?).' + target, r.text)))
        for dom in urlscan_domains:
            dom = dom + "." + target
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        # Developed BY ME
        apikey =  '006f48df28c3aca049dd5aab2b010df8b7b1fa10440c60914fdf074c398b670d'  #Done
        if target[:12] == "https://www.":
            target = target[12:]
        url = 'https://www.virustotal.com/vtapi/v2/domain/report'
        params = {'apikey':apikey,'domain':target}
        try:
            response = get(url, params=params)
            jdata = response.json()
            domains = sorted(jdata['subdomains'])
            for i in domains:
                try:
                    #print (f"{w}[{b}+{w}] {i.rstrip()} +> {gethostbyname(i.rstrip())}")
                    doms.write(i.rstrip() + '\n')
                except:
                    continue
        except(KeyError):
            exit("No domains found for %s" % target)
        except(ConnectionError):
            exit("Could not connect to www.virtustotal.com")
        with open("censys_domains.txt" , 'w')as ffc:ffc.write(Popen(f'censys subdomains {target}', shell=True, stdout=PIPE ).communicate()[0].decode())
        doms.close()
        del_repeat([f"{target}-subdomains.txt"])
        fxx = open(f"{target}-subdomains.txt" , 'r')
        print (f'{w}[{b}*{w}]{w} Success Collect {str(len(fxx.readlines()))} Subdomains in {target}-subdomains.txt')
        fxx.close()
        print (f'{w}[{g}*{w}] Done .')
    except KeyboardInterrupt :
        exit()
    except Exception as e:
        print (e)
        doms.close()
        with open("censys_domains.txt" , 'w')as ffc:ffc.write(Popen(f'censys subdomains {target}', shell=True, stdout=PIPE ).communicate()[0].decode())
        del_repeat([f"{target}-subdomains.txt"])
        fxx = open(f"{target}-subdomains.txt" , 'r')
        print (f'{w}[{b}*{w}]{w} Success Collect {str(len(fxx.readlines()))} Subdomains in {target}-subdomains.txt')
        fxx.close()
        print (f'{w}[{g}*{w}] Done .')
banner()
if len(argv) == 1:
    print ('Usages:')
    print ("""
-t domain to collect subdomains

Example:

1. ./{0} -t hackerone.com # Not https:// or http:// or www.

""".format(argv[0]))
else:
    try:
        if "-t" in argv[1:]:
            target = argv[argv.index('-t')+1]
        if "-t" not in argv[1:]:
            exit(f"{w}[{red}!{w}] Target Not Inserted")
        sub_collector(target)
    except Exception as e:
        print (e)
