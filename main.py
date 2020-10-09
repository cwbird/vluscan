# -*- coding: utf-8 -*-
#author: cwbird

import importlib
import configparser
config = configparser.ConfigParser()

def check(url,poc,trigger=""):
	if poc == r'全部漏洞':
		try:
			config.read('config.ini',encoding="utf-8-sig")
			exp_db = dict(config.items('vuln_db'))
     
			for exp_name,m in exp_db.items():
				if m =='':
					continue
				module = importlib.machinery.SourceFileLoader('exp',m).load_module()
				arg = url.strip()
				if 'http' in arg:

					rep = module.exp_check(arg)
				
					if rep == 1:
						trigger.emit("<font color='red'>警告！！！"+arg+"  存在"+exp_name+"漏洞</font>")
					elif rep == 2:
						trigger.emit(arg+'  不存在'+exp_name+'漏洞')
					else:
						trigger.emit(arg+'  无法访问')
				else:
					newurl = 'http://'+arg
					rep = module.exp_check(newurl)
				
					if rep == 1:
						trigger.emit("<font color='red'>警告！！！"+newurl+"  存在"+exp_name+"漏洞</font>")
					elif rep == 2:
						trigger.emit(newurl+'  不存在'+exp_name+'漏洞')
					else:
						trigger.emit(newurl+'  无法访问')

		except Exception as e:
			trigger.emit('[+]请检查exp是否可用')
	else:
		try:
			config.read('config.ini',encoding="utf-8-sig")
			exp_db = dict(config.items('vuln_db'))
			module = importlib.machinery.SourceFileLoader('exp', exp_db[poc]).load_module()

			arg = url.strip()

			if 'http' in arg:

					rep = module.exp_check(arg)
				
					if rep == 1:
						trigger.emit("<font color='red'>警告！！！"+arg+"  存在"+poc+"漏洞</font>")
					elif rep == 2:
						trigger.emit(arg+'  不存在'+poc+'漏洞')
					else:
						trigger.emit(arg+'  无法访问')
			else:
				newurl = 'http://'+arg
				rep = module.exp_check(newurl)
				
				if rep == 1:
					trigger.emit("<font color='red'>警告！！！"+newurl+"  存在"+poc+"漏洞</font>")
				elif rep == 2:
					trigger.emit(newurl+'  不存在'+poc+'漏洞')
				else:
					trigger.emit(newurl+'  无法访问')
		except Exception as e:
			trigger.emit('[+]请检查exp是否可用')


