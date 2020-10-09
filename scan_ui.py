# -*- coding: utf-8 -*-
#author: cwbird

import re
import sys
from PyQt5 import QtGui,QtCore,QtWidgets
import configparser
import importlib
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import datetime
from main_ui import *
import main
import requests
config = configparser.ConfigParser()


banner = '''                                            
 _   _  _   _  _      _   _  _____  _____   ___   _   _ 
| | | || | | || |    | \ | |/  ___|/  __ \ / _ \ | \ | |
| | | || | | || |    |  \| |\ `--. | /  \// /_\ \|  \| |
| | | || | | || |    | . ` | `--. \| |    |  _  || . ` |
\ \_/ /| |_| || |____| |\  |/\__/ /| \__/\| | | || |\  |
 \___/  \___/ \_____/\_| \_/\____/  \____/\_| |_/\_| \_/
                                                        
                                    ----by cwbird\n
version 1.0 \n本来想集成大量的框架exp并进行利用的，但是界面过于臃肿，还是一个框架一个框架的来吧
 '''

class Vlun_scan(QtWidgets.QMainWindow,QtWidgets.QApplication,Ui_MainWindow):
    def __init__(self):
        super(Vlun_scan, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.poc_list = self.exp_db().keys()
    
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)

        self.Ui.comm_perform.clicked.connect(self.go_exec)
        self.Ui.list_comboBox.addItems(self.poc_list)
        self.Ui.banner_out.append(banner)
        self.Ui.list_comboBox.currentIndexChanged.connect(self.list_print)

        self.Ui.subm_button.clicked.connect(self.check)
        self.Ui.upload.clicked.connect(self.geturl)
        self.Ui.piliang_scan.clicked.connect(self.batch_check)
        self.Ui.action1.triggered.connect(self.about)
        self.Ui.action1_gengxin.triggered.connect(self.update)
        self.Ui.action1_daochu.triggered.connect(self.save)
        config = configparser.ConfigParser()




        
        



    def exp_db(self):
        try:
            config.read('config.ini',encoding="utf-8-sig")
            return dict(config.items('vuln_db'))
        except:
            box = QtWidgets.QMessageBox()
            box.about(self, "启动检查",
                  "       请检查配置文件是否存在")





    def list_print(self):
        self.poc = self.Ui.list_comboBox.currentText()
        self.Ui.log_browser.clear()
        self.Ui.log_browser.append('您选择的是：'+self.poc)

    def save(self):
        box = QtWidgets.QMessageBox()
        with open('result.txt','a') as f:
            f.write(self.Ui.batch_Browser.toPlainText())

    def update(self):
        box = QtWidgets.QMessageBox()
        box.about(self, "更新",
                  "       暂不支持在线更新")

    def about(self):
        box = QtWidgets.QMessageBox()
        box.about(self, "关于",
                  "\t\t\t关于\n       此程序为漏洞扫描利用工具，请勿非法使用！\n\t\t\t   Powered by --cwbird\n联系作者：1600096953@qq.com")

    def scan_log(self,scan_log):
        self.Ui.log_browser.append(scan_log)

    def batch_log(self,scan_log):
        self.Ui.batch_Browser.append(scan_log)


    def check(self):
        self.Thread_check = MyThread_check()
        self.url = self.Ui.url_input.text()
        self.poc = self.Ui.list_comboBox.currentText()
        res = re.match("(http|https|ftp)://[^\s]+", self.url)
        if res == None:
            self.Ui.log_browser.append(self.url+'  url格式不正确')
        else:
            #启动线程
            self.Thread_check.url=self.url
            self.Thread_check.poc=self.poc

            self.Thread_check.scan_Signal.connect(self.scan_log)
            self.Thread_check.start()

            
            

    def go_exec(self):
        self.url = self.Ui.url_input.text()
        self.poc = self.Ui.list_comboBox.currentText()
        self.cmd = self.Ui.commd_input.text()
        self.Ui.cmd_out.clear()
        res = re.match("(http|https|ftp)://[^\s]+", self.url)
        if res == None:
            self.Ui.log_browser.append(self.url+'  url格式不正确')
        else:
            if self.poc == r'全部漏洞':
                self.Ui.log_browser.append('[+]请选择要执行命令的漏洞')
            else:
                module = importlib.machinery.SourceFileLoader('exp', self.exp_db()[self.poc]).load_module()
                self.rep = module.exp_cmd(self.url,self.cmd)
                if self.rep ==3:
                    self.Ui.log_browser.append(self.url+'  无法访问')
                else:
                    self.Ui.cmd_out.append(self.rep)
    def geturl(self):
        filename = self.Ui.file_input.text()
        self.Ui.batch_Browser.clear()
        urllist = []
        if filename != '':
            try:
                with open(filename,'r') as f:
                    urls = f.readlines()
                for url in urls:
                    url = url.strip()
                    urllist.append(url)
                self.Ui.batch_Browser.append('[+]导入文件为：'+filename)
                self.Ui.batch_Browser.append('[+]共计：'+str(len(urllist))+'个url')
            except:
                self.Ui.batch_Browser.append('[+]文件路径有误：'+filename)
            return urllist
        else:
            return 0


    def batch_check(self):
        starttime = datetime.datetime.now()
        urllist = self.geturl()
        self.poc = self.Ui.list_comboBox.currentText()
        if urllist ==0:
            self.Ui.batch_Browser.append('[+]警告！！！请先导入url')
        elif urllist == []:
            self.Ui.batch_Browser.append('[+]警告！！！文件内容为空')

        else:
            
            self.Batch_check = MyBatch_check()
            self.Batch_check.urllist = urllist
            self.Batch_check.poc = self.poc
            self.Batch_check.scan_Signal.connect(self.batch_log)
            self.Batch_check.start()





        endtime = datetime.datetime.now()
        self.Ui.batch_Browser.append(str(endtime - starttime))


class MyThread_check(QtCore.QThread):
    scan_Signal = QtCore.pyqtSignal(str) # 初始化scan_Signal用来传递日志文本，str表示接收参数
    

    def __init__(self):
        super(MyThread_check, self).__init__()
        self.url=''
        self.poc=''

    def run(self):
        self.scan_Signal.emit("启动扫描<br/>-----------------------------------------------------------")
        main.check(self.url,self.poc,trigger=self.scan_Signal)
        
class MyBatch_check(QtCore.QThread):
    scan_Signal = QtCore.pyqtSignal(str) # 初始化scan_Signal用来传递日志文本，str表示接收参数
    

    def __init__(self):
        super(MyBatch_check, self).__init__()
        self.urllist=[]
        self.poc=''


    def run(self):
        self.scan_Signal.emit("启动扫描<br/>-----------------------------------------------------------")
        for url in self.urllist:
            main.check(url,self.poc,trigger=self.scan_Signal)
        self.scan_Signal.emit("扫描完成<br/>-----------------------------------------------------------")



        








	

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Vlun_scan()
    ui.show()
    sys.exit(app.exec_())
