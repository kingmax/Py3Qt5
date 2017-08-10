#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/10
"""

import unittest

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
        super().__init__()
        self.initUI()
        
    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtWidgets.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        
        btn_quit = QtWidgets.QPushButton('Quit', self)
        btn_quit.clicked.connect(self.exit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(50, 100)
        btn_quit.setToolTip('<b>Exit the app</b>')
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QtGui.QIcon(r'D:\2017.6.6\jason.jpg'))
        
        self.show()
    
    #----------------------------------------------------------------------
    def exit(self):
        """"""
        QtCore.QCoreApplication.instance().quit()
    

if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())