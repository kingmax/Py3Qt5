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
        
        super(Window, self).__init__()
        self.initUI()
        
    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        labelA = QtWidgets.QLabel('Zetcode', self)
        labelA.move(15, 10)
        
        labelB = QtWidgets.QLabel('tutorials', self)
        labelB.move(35, 40)
        
        labelC = QtWidgets.QLabel('for programmers', self)
        labelC.move(55, 70)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()
    
    

if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())