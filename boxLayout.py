#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/10
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

########################################################################
class Window(QtWidgets.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        super(Window, self).__init__()
        self.initUI()

    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        btnOK = QtWidgets.QPushButton('OK')
        btnCancel = QtWidgets.QPushButton('Cancel')
        
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnOK)
        hbox.addWidget(btnCancel)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Buttons')
        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())