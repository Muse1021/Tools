# -*-coding: utf-8 -*-

from ReQLineEdit import Edit
from PyQt4 import QtGui,QtCore
import os,subprocess,time,re,sys
from Functions import *
reload(sys)
sys.setdefaultencoding( "utf-8" )
class Exemple(QFunction):
    def __init__(self):
        super(Exemple,self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(500,500)
        self.center()
        self.setWindowTitle(u'工具')
        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        #安装
        btn = QtGui.QPushButton(u'安装',self)
        btn.clicked.connect(self.btn_install)
        btn.resize(btn.sizeHint())
        btn.move(400,100)
        #卸载
        btn_uninstall = QtGui.QPushButton(u'卸载',self)
        btn_uninstall.clicked.connect(self.btn_uninstall)
        #btn_uninstall.resize(btn_uninstall.sizeHint())
        btn_uninstall.move(300,100)
        #刷新列表
        #btn_re = QtGui.QToolButton(self)
        #btn_re.clicked.connect(self.devices_list)
        #btn_re.resize(btn_uninstall.sizeHint())
        #btn_re.setIcon(QtGui.QIcon("timg.jpg"))
        #btn_re.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        btn_re = QtGui.QPushButton(self)
        btn_re.setStyleSheet("QPushButton{background-image:url(1.png);width:20px;height:20px;padding-top:0px;}")
        btn_re.clicked.connect(self.devices_list)
        btn_re.move(440,45)
        #清除数据
        btn_re = QtGui.QPushButton(u'清除数据',self)
        btn_re.clicked.connect(self.btn_clean)
        btn_re.move(100,100)
        #截图
        btn_re = QtGui.QPushButton(u'截图',self)
        btn_re.clicked.connect(self.screenshot)
        btn_re.move(200,100)
        #打开cm
        btn_re = QtGui.QPushButton(u'打开cm',self)
        btn_re.clicked.connect(self.btn_open)
        btn_re.move(0,100)		
        #手机列表下拉框
        string_list = [u'无设备']
        self.combo = QtGui.QComboBox(self)
        self.combo.addItems(string_list)
        self.combo.resize(80, 20)
        self.combo.move(350,45)
        #输入框
        self.inputtext =  QtGui.QLineEdit(self)
        self.inputtext.setGeometry(QtCore.QRect(20, 140, 300, 30))
        self.inputtext.setText("")
        #输入按钮
        btn_inp = QtGui.QPushButton(u'输入',self)
        btn_inp.clicked.connect(self.InputText)
        btn_inp.resize(btn_uninstall.sizeHint())
        btn_inp.move(350,145)
        #apk地址输入框
        self.apkpath =Edit(self)
        self.apkpath.setGeometry(QtCore.QRect(20, 40, 300, 30))
        self.apkpath.setText("")

#        layout = QtGui.QVBoxLayout(self)
#        layout.addWidget(self.apkpath)
#        self.setLayout(layout)
        self.show()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ic = Exemple()
    sys.exit(app.exec_())