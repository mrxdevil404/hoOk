import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from sys import argv
from os.path import isfile
def pass_to_burp( name_f ):
    proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
    with open(name_f , 'r')as f:
        for url in f.readlines():
            url = url.rstrip()
            if not url.startswith("https://"):
                url = "https://" + url
            req = requests.get(url ,verify=False , proxies=proxies)
if "-f" in argv[1:]:
    name_f = argv[argv.index('-f')+1]
    if not isfile(name_f):
        exit("[!] File Not Found")
    pass_to_burp( name_f )
if "-f" not in argv[1:]:
    exit("[!] Target Not Inserted")