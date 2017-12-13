# -*-coding: utf-8 -*-
from chosedevices import get_devices
from PyQt4 import QtGui,QtCore
import os,subprocess,time,re,sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class Edit(QtGui.QLineEdit):
    def __init__(self, parent):
        super(Edit, self).__init__(parent)
        self.setAcceptDrops(True)
        #self.setDragDropMode(QAbstractItemView.InternalMove)
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Edit, self).dragEnterEvent(event)
    def dragMoveEvent(self, event):
        super(Edit, self).dragMoveEvent(event)
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            #遍历输出拖动进来的所有文件路径
            for url in event.mimeData().urls():
                strs =  url.toLocalFile()
                self.setText(strs)
            event.acceptProposedAction()
        else:
            super(Edit,self).dropEvent(event)
class Exemple(QtGui.QWidget):
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
        btn_uninstall.resize(btn_uninstall.sizeHint())
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
        btn_re.resize(btn_uninstall.sizeHint())
        btn_re.move(100,100)
        #截图
        btn_re = QtGui.QPushButton(u'截图',self)
        btn_re.clicked.connect(self.screenshot)
        btn_re.resize(btn_uninstall.sizeHint())
        btn_re.move(200,100)
        #打开cm
        btn_re = QtGui.QPushButton(u'打开cm',self)
        btn_re.clicked.connect(self.btn_open)
        btn_re.resize(btn_uninstall.sizeHint())
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
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def btn_install(self):
        print "3232323: " ,self.combo.currentText()
        path_str = str(self.apkpath.text()).decode('UTF-8').encode('GBK')
        install_cmd = "adb -s %s install -r "%(self.lists[str(self.combo.currentText())])+path_str
        print(install_cmd)
        Poplog = subprocess.Popen(str(install_cmd), shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
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
        self.lists = get_devices()
        strs = []
        if len(self.lists.keys())>0:
            for i in self.lists.keys():
                strs.append(i)
        else:
            strs = [u"无"]
        self.combo.clear()
        self.combo.addItems(strs)
    def InputText(self):
        text = str(self.inputtext.text())
        print(text)
        Inputtext = "adb -s %s shell input text %s"%((self.lists[str(self.combo.currentText())]),text)
        print(Inputtext)
        Poplog = subprocess.Popen(Inputtext, shell=True, stdout=subprocess.PIPE).stdout
        Poplog.readlines()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ic = Exemple()
    sys.exit(app.exec_())