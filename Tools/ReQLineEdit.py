# -*-coding: utf-8 -*-

from PyQt4 import QtGui,QtCore
import sys
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