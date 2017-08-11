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
        btn1 = QtWidgets.QPushButton('Button 1', self)
        btn1.move(30, 50)
        btn1.clicked.connect(self.buttonClick)
        
        btn2 = QtWidgets.QPushButton('Button 2', self)
        btn2.move(150, 50)
        btn2.clicked.connect(self.buttonClick)
        
        self.status = self.statusBar()
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('MyWindow')
        self.show()

    #----------------------------------------------------------------------
    def buttonClick(self):
        """"""
        sender = self.sender()
        self.status.showMessage(sender.text() + ' was pressed')
        
    #----------------------------------------------------------------------
    def keyPressEvent(self, event):
        """"""
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())