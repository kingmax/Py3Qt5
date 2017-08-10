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
        exitAct = QtWidgets.QAction(QtGui.QIcon(r'D:\2017.6.6\jason.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.quit)
        
        self.statusBar()
        
        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAct)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.setWindowIcon(QtGui.QIcon())
        
        self.show()
        
    #----------------------------------------------------------------------
    def quit(self):
        """"""
        QtWidgets.qApp.quit()
    
    

if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())