# -*-coding: utf-8 -*-
from PyQt4 import QtGui,QtCore
import os,time,re,sys
from Utils import *
reload(sys)
sys.setdefaultencoding( "utf-8" )
class QFunction(Utils):
    def __init__(self):
        super(QFunction,self).__init__()
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def btn_install(self):
        if self.check_connect() != False:
            try:
                print "combo.currentText: " ,self.combo.currentText()
                path_str = self.check_apkpath()
                if path_str:
                    install_cmd = "adb -s %s install -r "%(self.get_combo_currentText())+path_str
                    print "install_cmd",install_cmd
                    self.cmd_show(install_cmd)
            except Exception,e:
                print "fatall",e
                QtGui.QMessageBox.about(self,"",str(e))
    def btn_uninstal(self):
        uninstall_cmd = "adb -s %s uninstall com.cleanmaster.mguard_cn"%self.get_combo_currentText()
        self.single_cmd(uninstall_cmd)
    def btn_uninstall(self):
        if self.check_connect() != False:
            uninstall_cmd = "adb -s %s uninstall com.cleanmaster.mguard_cn"%(self.get_combo_currentText())
            self.cmd_show(uninstall_cmd)
    def btn_clean(self):
        if self.check_connect() != False:
            clear_cmd = "adb -s %s shell pm clear com.cleanmaster.mguard_cn"%(self.get_combo_currentText())
            self.cmd_show(clear_cmd)
    def btn_open(self):
        open_cmd = "adb -s %s shell am  start com.cleanmaster.mguard_cn/com.keniu.security.main.MainActivity"%(self.get_combo_currentText())
        self.cmd(open_cmd)
    def screenshot(self):
        screenshot = "adb -s %s shell /system/bin/screencap -p /sdcard/screenshot.png"%(self.get_combo_currentText())
        pic_name = str(int(time.time()))+".png"
        screenshot_pull = "adb -s %s pull /sdcard/screenshot.png D:\screenshot\%s"%((self.get_combo_currentText()),pic_name)
        #subprocess.Popen(screenshot,shell=True, stdout=subprocess.PIPE).stdout
        self.cmd(screenshot)
        if  os.path.exists("D:\screenshot"):
            pass
        else:
            os.mkdir("D:\screenshot")
        #Poplog = subprocess.Popen(screenshot_pull, shell=True, stdout=subprocess.PIPE).stdout
        #Poplog.readlines()
        self.cmd(screenshot_pull)
    def devices_list(self):
        model_list = self.checkdevice()
        if model_list == False:
            pass
        else:
            self.lists = model_list
            strs = []
            if len(self.lists.keys())>0:
                for i in self.lists.keys():
                    strs.append(i)
            else:
                strs = [u"无设备"]
            self.combo.clear()
            self.combo.addItems(strs)
    def InputText(self):
        text = str(self.inputtext.text())
        print(text)
        Inputtext = "adb -s %s shell input text %s"%((self.get_combo_currentText()),text)
        print(Inputtext)
        Poplog = subprocess.Popen(Inputtext, shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
