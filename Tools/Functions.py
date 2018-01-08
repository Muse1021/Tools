# -*-coding: utf-8 -*-
from PyQt4 import QtGui,QtCore
from ReMessage import Message
import os,subprocess,time,re,sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class QFunction(QtGui.QWidget):
    def __init__(self):
        super(QFunction,self).__init__()
    def get_devices1(self):
        logcmd = "adb devices"
        #Poplog = subprocess.Popen(logcmd,stderr=subprocess.PIPE)
        #Poplog = os.popen(logcmd)
        Poplog = subprocess.Popen(logcmd, shell=True, stdout=subprocess.PIPE).stdout
        devices = Poplog.readlines()
        print "devices:",devices
        devices_list = []
        model_list ={}
        for i in devices:
            if 'devices' not in i and len(i.split()) > 0:
                #print "i: ",i
                #print "len: ",len(i)
                devices_list.append(i.split()[0])
        device_number = len(devices_list)
        print(devices_list)
        if device_number == 0 :
            print "NO decices !!"
        else:
            for i in range(device_number):
                print "11111:",devices_list[i]

                de = "adb -s %s shell  getprop ro.product.model" % (devices_list[i])
                Poplog = subprocess.Popen(de, shell=True, stdout=subprocess.PIPE).stdout
                strs = (Poplog.readlines()[0]).strip()
                model_list[strs] = devices_list[i]

        return model_list
    def get_devices(self):
        logcmd = "adb devices"
        Poplog = subprocess.Popen(logcmd, shell=True, stdout=subprocess.PIPE).stdout
        devices = Poplog.readlines()
        print "devices:",devices
        devices_list = []
        model_list ={}
        for i in devices:
            if 'devices' not in i and len(i.split()) > 0:
                devices_list.append(i.split()[0])
        device_number = len(devices_list) 
        print(devices_list)
        if device_number == 0 :
            return False
        else:
            for i in range(device_number):
                print "11111:",devices_list[i]

                de = "adb -s %s shell  getprop ro.product.model" % (devices_list[i])
                print de
                try:
                    Poplog = subprocess.Popen(de, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    g = Poplog.stdout.readlines()
                    b = Poplog.stderr.read()
                    strs = (g[0]).strip()
                    model_list[strs] = devices_list[i]                    
                except Exception as e:
                    if b != "":
                        QtGui.QMessageBox.about(self,"",b)
                    else:
                        QtGui.QMessageBox.about(self,"",str(e))
                    return False
            return model_list
    def checkdevice(self):
        model_list = self.get_devices()
        if model_list == False:
            QtGui.QMessageBox.about(self,"",u"无设备！！")
            return False
        else:
            return model_list
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def btn_install1(self):
        print "3232323: " ,self.combo.currentText()
        path_str = str(self.apkpath.text()).decode('UTF-8').encode('GBK')
        install_cmd = "adb -s %s install -r "%(self.lists[str(self.combo.currentText())])+path_str
        print(install_cmd)
        Poplog = subprocess.Popen(str(install_cmd), shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
    def btn_install(self):
        if self.checkdevice() != False:
            try:
                print "3232323: " ,self.combo.currentText()
                path_str = str(self.apkpath.text()).decode('UTF-8').encode('GBK')
                install_cmd = "adb -s %s install -r "%(self.lists[str(self.combo.currentText())])+path_str
                print(install_cmd)
                Poplog = subprocess.Popen(str(install_cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            except Exception,e:
                print "fatall",e
                QtGui.QMessageBox(self,"",e)
    def btn_uninstall(self):
        uninstall_cmd = "adb -s %s uninstall com.cleanmaster.mguard_cn"%(self.lists[str(self.combo.currentText())])
        Poplog = subprocess.Popen(uninstall_cmd, shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
    def btn_clean(self):
        uninstall_cmd = "adb -s %s shell pm clear com.cleanmaster.mguard_cn"%(self.lists[str(self.combo.currentText())])
        Poplog = subprocess.Popen(uninstall_cmd, shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
    def btn_open(self):
        uninstall_cmd = "adb -s %s shell am  start com.cleanmaster.mguard_cn/com.keniu.security.main.MainActivity"%(self.lists[str(self.combo.currentText())])
        Poplog = subprocess.Popen(uninstall_cmd, shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
    def screenshot(self):
        screenshot = "adb -s %s shell /system/bin/screencap -p /sdcard/screenshot.png"%(self.lists[str(self.combo.currentText())])
        pic_name = str(int(time.time()))+".png"
        screenshot_pull = "adb -s %s pull /sdcard/screenshot.png D:\screenshot\%s"%((self.lists[str(self.combo.currentText())]),pic_name)
        subprocess.Popen(screenshot,shell=True, stdout=subprocess.PIPE).stdout
        if  os.path.exists("D:\screenshot"):
            pass
        else:
            os.mkdir("D:\screenshot")
        Poplog = subprocess.Popen(screenshot_pull, shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
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
        Inputtext = "adb -s %s shell input text %s"%((self.lists[str(self.combo.currentText())]),text)
        print(Inputtext)
        Poplog = subprocess.Popen(Inputtext, shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
