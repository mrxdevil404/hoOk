import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from json import loads , load , dumps
from subprocess import Popen , PIPE
from platform import system as iden
from webbrowser import open as op_w
from os import system , listdir
from bs4 import BeautifulSoup
from os.path import isfile
from datetime import date
from colorama import Fore
from time import strftime
from random import choice
from sys import argv
from re import *
w = Fore.WHITE
red = Fore.RED
b = Fore.BLUE
g = Fore.GREEN
c = Fore.CYAN
def pass_to_burp():

    proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
    for file_n in listdir():
        if file_n.endswith(".txt") and file_n != "censys_domains.txt":
            with open(file_n , 'r')as f:
                for url in f.readlines():
                    url = url.rstrip()
                    if not url.startswith("https://"):
                        url = "https://" + url
                    req = requests.get(url ,verify=False , proxies=proxies)

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
                    |_| |_|\___/ \___/|_|\_\ V 1.1
                        
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

def facebook_sub( target ):

    if iden() == 'Windows':
        op_w(f"https://developers.facebook.com/tools/ct/search?query={target}")
    else:
        print (f"{w}[{g}+{w}] Open Link: https://developers.facebook.com/tools/ct/search?query={target}")
    print (f"{w}[{g}+{w}] Open Link: https://developers.facebook.com/tools/ct/async/\n{w}[{red}+{w}] Add {target} in Subscriptions to Recieve the new subdomains of target")

def sub_collector(target):

    doms = open(f"{target}-subdomains.txt" , 'a')
    try:
        print (f'{w}[{red}+{w}] {g}[{strftime("%H:%M:%S")}] {g} Start .')
        print (f"{w}[{b}*{w}] {c}subdomainfinder.c99")
        print (f"{w}[{b}*{w}] {c}otx.alienvault")
        print (f"{w}[{b}*{w}] {c}securitytrails")
        print (f"{w}[{b}*{w}] {c}hackertarget")
        print (f"{w}[{b}*{w}] {c}rapiddns.io")
        print (f"{w}[{b}*{w}] {c}whoisxmlapi")
        print (f"{w}[{b}*{w}] {c}riddler.io")
        print (f"{w}[{b}*{w}] {c}virustotal")
        print (f"{w}[{b}*{w}] {c}facebook")
        print (f"{w}[{b}*{w}] {c}urlscan")
        print (f"{w}[{b}*{w}] {c}jldc.me")
        print (f"{w}[{b}*{w}] {c}censys")
        print (f"{w}[{b}*{w}] {c}crt.sh{w}")
        if not isfile("whoisxmlapi.txt"):
            print(f"{w}[{red}!{w}] add api_key of https://subdomains.whoisxmlapi.com to collect from whoisxmlapi")
        nn = 0
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}
        for month in range(6 , 13):
            for i in range(1 , 31):
                if nn != 0:
                    break
                my_date = date(date.today().year - 1 , month , i)
                html_doc_1 = requests.get(f"https://subdomainfinder.c99.nl/scans/{my_date}/{target}" ,allow_redirects=True , headers=headers)
                if not "Something went wrong while scanning" in html_doc_1.text:
                    soup = BeautifulSoup(html_doc_1.text, 'html.parser')
                    for sub in soup.find_all("a"):
                        if sub.get("href"):
                            if target in sub.get("href") and "subdomainfinder.c99.nl/scans" not in sub.get("href"):
                                print (sub.get("href")[2:])
                                doms.write(sub.get("href")[2:] + '\n')
                                nn += 1
            if nn != 0:
                break
        if isfile("whoisxmlapi.txt"):
            try:
                api_key = open("whoisxmlapi.txt" , 'r').readlines()
                req = requests.get(f"https://subdomains.whoisxmlapi.com/api/v1?apiKey={choice(api_key)}&domainName={target}")
                req_n = loads(req.text)
                req_m = req_n["result"]["records"]
                for sea in req_m:
                    print (sea['domain'])
                    doms.write(sea['domain'] + '\n')
                for n in range(1 , 101):
                    html_doc_2 = requests.get(f"https://rapiddns.io/subdomain/{target}?page={str(n)}#result" , allow_redirects=True , headers=headers)
                    soup = BeautifulSoup(html_doc_2.text, 'html.parser')
                    for sub in soup.find_all("td"):
                        if sub.text.endswith(target):
                            print (sub.text)
                            for sub_ in sub.text.split('\n'):
                                doms.write(sub_ + '\n')
            except Exception as e:
                print (e)
                print (f"{red} api_key is no longer valid")
        req = requests.get(f"https://api.securitytrails.com/v1/domain/{target}/subdomains?apikey=lEDJ6fVras9R8doewLFuJ6WnV0gumSR6").text
        for sub in loads(req)["subdomains"]:
            print (sub + '.' + target)
            doms.write(sub + '.' + target + '\n')
        req = requests.get(f"https://jldc.me/anubis/subdomains/{target}" , headers=headers).text
        for sub in loads(req):
            print (sub)
            doms.write(sub + '\n')
        # Developed By Me This Function Coded In AORT Tool from the next code except virustotal depart
        r = requests.get("https://crt.sh/?q=" + target + "&output=json", timeout=20)
        f_json = dumps(loads(r.text), indent=4)
        crt_domains = sorted(set(findall(r'"common_name": "(.*?)"', f_json)))
        for dom in crt_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{target}/passive_dns", timeout=20)
        alienvault_domains = sorted(set(findall(r'"hostname": "(.*?)"', r.text)))
        for dom in alienvault_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={target}", timeout=20)
        hackertarget_domains = findall(r'(.*?),', r.text)
        for dom in hackertarget_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = requests.get(f"https://riddler.io/search/exportcsv?q=pld:{target}", timeout=20)
        riddler_domains = findall(r'\[.*?\]",.*?,(.*?),\[', r.text)
        for dom in riddler_domains:
            if dom.endswith(target):
                print (dom)
                doms.write(dom + '\n')
        r = requests.get(f"https://urlscan.io/api/v1/search/?q={target}", timeout=20)
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
            response = requests.get(url, params=params)
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
        with open("censys_domains.txt" , 'a')as ffc:ffc.write(Popen(f'censys subdomains {target}', shell=True, stdout=PIPE ).communicate()[0].decode())
        doms.close()
        del_repeat([f"{target}-subdomains.txt"])
        fxx = open(f"{target}-subdomains.txt" , 'r')
        print (f'{w}[{b}*{w}]{w} Success Collect {str(len(fxx.readlines()))} Subdomains in {target}-subdomains.txt')
        fxx.close()
        print (f"{w}[{b}*{w}] Reference: {html_doc_1.url}")
        facebook_sub( target )
        print (f'{w}[{g}*{w}] Done .')
    except KeyboardInterrupt :
        exit()
    except Exception as e:
        print (e)
        doms.close()
        with open("censys_domains.txt" , 'a')as ffc:ffc.write(Popen(f'censys subdomains {target}', shell=True, stdout=PIPE ).communicate()[0].decode())
        del_repeat([f"{target}-subdomains.txt"])
        fxx = open(f"{target}-subdomains.txt" , 'r')
        print (f'{w}[{b}*{w}]{w} Success Collect {str(len(fxx.readlines()))} Subdomains in {target}-subdomains.txt')
        fxx.close()
        print (f"{w}[{b}*{w}] Reference: {html_doc_1.url}")
        facebook_sub( target )
        print (f'{w}[{g}*{w}] Done .')
        if "-burp" in argv[1:] and "-f" not in argv[1:]:
            print (f"{w}[{g}+{w}] Pass Results to burp")
            pass_to_burp()
banner()
if len(argv) == 1:
    print ('Usages:')
    print ("""
-t    : domain to collect subdomains
-f    : input file
-burp : pass results to burp

Example:

1. ./{0} -t hackerone.com -burp # Not https:// or http:// or www.
2. ./{0} -f domains.txt -burp
""".format(argv[0]))
else:
    try:
        if "-t" in argv[1:]:
            target = argv[argv.index('-t')+1]
        if "-f" in argv[1:]:
            name_f = argv[argv.index('-f')+1]
            if isfile(name_f):
                with open(name_f , 'r')as f:
                    for new_target in f.readlines():
                        new_target = new_target.rstrip()
                        if new_target.startswith("https://"):
                            new_target = new_target.replace("https://" , '')
                        if new_target.startswith("http://"):
                            new_target = new_target.replace("http://" , '')
                        if new_target.startswith("www."):
                            new_target = new_target.replace("www." , '')
                        sub_collector( new_target )
                if  "-burp" in argv[1:]:
                    print (f"{w}[{g}+{w}] Pass Results to burp")
                    pass_to_burp()
            else:
                exit(f"{w}[{red}!{w}] File Not Found")
        if "-f" not in argv[1:]:
            sub_collector(target)
    except Exception as e:
        print (e)
