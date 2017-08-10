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
        self.exitAct = QtWidgets.QAction(QtGui.QIcon(r'D:\2017.6.6\jason.jpg'), '&Exit', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(self.close)
        
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(self.exitAct)
        
        toolBar = self.addToolBar('main')
        toolBar.addAction(self.exitAct)
        
        self.txtEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.txtEdit)
        
        self.statusBar()
        
        self.show()
    
    

if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())