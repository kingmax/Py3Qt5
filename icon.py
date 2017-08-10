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
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon(r'D:\2017.6.6\jason.jpg'))
        
        self.show()
    
    


if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())