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
        self.btn = QtWidgets.QPushButton('Input your name', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtWidgets.QLineEdit(self)
        self.le.move(130, 20)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Input Dialog')
        self.show()
        
    #----------------------------------------------------------------------
    def showDialog(self):
        """"""
        txt, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(txt)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())