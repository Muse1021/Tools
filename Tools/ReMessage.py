# -*-coding:utf-8 -*-
from PyQt4 import QtCore,QtGui

class Message(QtGui.QMessageBox):
    def __init__(self,parent):
        super(Message,self).__init__(parent)
        #self.n = n
        #self.Stuation()
        self.showtheerr()
    def Stuation(self):
        if self.n == 1:
            self.about(self,'Test',U"出现错误！！！")
        if self.n ==2:
            self.about(self,"test"U"卸载成功！！！")
    def showtheerr(self,errstr):
        self.about(self,"Error",errstr)


            
