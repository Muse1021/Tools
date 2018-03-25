# -*-coding: utf-8 -*-
import subprocess,re
from PyQt4 import QtGui,QtCore
from Func_thread import Thread_func
#QtGui.QWidget
class Utils(QtGui.QWidget):
    def cmd(self,cmd):
        Poplog = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        a = Poplog.stdout.readlines()
        b = Poplog.stderr.read()
        print b
        if a:
            print a
            return a
        #QtGui.QMessageBox.about(self,u"错误",b)
        self.d.Signal_cmd.connect(self.Show_MessageBox)
        self.d.Signal_cmd.emit([u"错误",b])
        return False
    def cmd_show(self,cmd1):
        result = self.cmd(cmd1)
        if "Success"in str(result):
            #QtGui.QMessageBox.about(self,u"提示",u"成功")
            self.d.Signal_cmd_show.connect(self.Show_MessageBox)
            self.d.Signal_cmd_show.emit([u"提示",u"成功"])
        else:
            #QtGui.QMessageBox.about(self,u"错误",result[0])
            self.d.Signal_cmd_show.connect(self.Show_MessageBox)
            self.d.Signal_cmd_show.emit([u"错误",result[0]])
    def checkdevice(self):
        model_list = self.get_devices()
        if model_list == False:
            #QtGui.QMessageBox.about(self,"",u"无设备！！")
            return False
        else:
            return model_list
    def check_connect(self):
        try:
            connect = "adb -s %s get-state "%(self.lists[str(self.combo.currentText())])
        except:
            #QtGui.QMessageBox.about(self,u"错误",u"设备未连接！！")
            self.d.Signal_check_connect.connect(self.Show_MessageBox)
            self.d.Signal_check_connect.emit([u"错误",u"设备未连接！！"])
            return False
        res = self.cmd(connect)
        print "res: ",res
        if "device" not in str(res) :
            #QtGui.QMessageBox.about(self,u"错误",u"设备未连接！！")
            self.d.Signal_check_connect.connect(self.Show_MessageBox)
            self.d.Signal_check_connect.emit([u"错误",u"设备未连接！！"])
            return False
    def check_apkpath(self):
        path_str = str(self.apkpath.text()).decode('UTF-8').encode('GBK')
        if ".apk" in path_str:
            return path_str
        else:
            #QtGui.QMessageBox.about(self,u"错误",u"请正确输入！！")
            self.d.Signal_check_apkpath.connect(self.Show_MessageBox)
            self.d.Signal_check_apkpath.emit([u"错误",u"请正确输入！！"])
    def get_combo_currentText(self):
        try:
            return self.lists[str(self.combo.currentText())]
        except:
            return False
    def single_cmd(self,cmd):
        if self.check_connect() != False:
            self.cmd_show(cmd)
    def get_devices(self):
        logcmd = "adb devices"
        #Poplog = subprocess.Popen(logcmd, shell=True, stdout=subprocess.PIPE).stdout
        #devices = Poplog.readlines()
        devices = self.cmd(logcmd)
        if devices:
            print "devices:",devices
        else:
            return False
        devices_list = []
        model_list ={}
        for i in devices:
            if not re.search('devices|daemon',i) and len(i.split()) > 0:
                devices_list.append(i.split()[0])
        device_number = len(devices_list)
        print(devices_list)
        if device_number == 0 :
            #QtGui.QMessageBox.about(self,"",u"无设备！！")
            self.d.Signal_get_devices.connect(self.Show_MessageBox)
            self.d.Signal_get_devices.emit([u"错误",u"无设备！！"])
            return False
        else:
            for i in range(device_number):
                print "devices_list: ",devices_list[i]

                de = "adb -s %s shell  getprop ro.product.model" % (devices_list[i])
                print de
                try:
                    g = self.cmd(de)
                    if g:
                        strs = (g[0]).strip()
                        model_list[strs] = devices_list[i]
                    else:
                        return False
                except Exception as e:
                    #QtGui.QMessageBox.about(self,u"错误",str(e))
                    self.d.Signal_get_devices.connect(self.Show_MessageBox)
                    self.d.Signal_get_devices.emit([u"错误",str(e)])
                    return False
            return model_list
    def Show_MessageBox(self,lists):
        title =lists[0]
        content =lists[1]
        QtGui.QMessageBox.about(self,title,content)



