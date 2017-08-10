#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/10
"""

import unittest

import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

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
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        
        newAct = QtWidgets.QAction('New', self)
        fileMenu.addAction(newAct)        
        
        impMenu = QtWidgets.QMenu('&Import', self)
        impAct = QtWidgets.QAction('Import mail', self)
        impMenu.addAction(impAct)
        fileMenu.addMenu(impMenu)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show() 
    
    

if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())