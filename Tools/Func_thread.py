# -*-coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
class Thread_func(QtCore.QThread):
    Signal_cmd = QtCore.pyqtSignal(list)
    Signal_cmd_show = QtCore.pyqtSignal(list)
    Signal_check_apkpath = QtCore.pyqtSignal(list)
    Signal_check_connect = QtCore.pyqtSignal(list)
    Signal_get_devices = QtCore.pyqtSignal(list)
    def __init__(self,f):
        super(Thread_func,self).__init__()
        self.f = f
    def run(self):
        self.f()