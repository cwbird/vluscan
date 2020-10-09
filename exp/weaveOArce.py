import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.58',
	'Accept':'Accept: */*',
	'Content-Type':'application/x-www-form-urlencoded',
	'Connection':'Keep-Alive'
}


def exp_check(url):

    try:
        r = requests.get(url+"/weaver/bsh.servlet.BshServlet/",verify= False,timeout=5)
        print(r.url)
        code = r.status_code
        print(code)
        
        if code == 200:
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    pass