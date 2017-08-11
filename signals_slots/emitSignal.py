#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/11
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

import time
########################################################################
class Communicate(QtCore.QObject):
    """"""
    closeApp = QtCore.pyqtSignal()
    

########################################################################
class Window(QtWidgets.QMainWindow):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        super(Window, self).__init__()
        self.initUI()

    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Emit signal')
        self.show()

    #----------------------------------------------------------------------
    def mousePressEvent(self, event):
        """"""
        self.statusBar().showMessage('emit signal...')
        time.sleep(0.5)
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())