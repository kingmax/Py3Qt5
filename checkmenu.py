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
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.setWindowIcon(QtGui.QIcon(r'd:\2017.06.06\jason.jpg'))
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        
        menuBar = self.menuBar()
        viewMenu = QtWidgets.QMenu('&View', self)
        viewStatAct = QtWidgets.QAction('V&iew statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleStatus)
        viewMenu.addAction(viewStatAct)
        menuBar.addMenu(viewMenu)
        
        
    #----------------------------------------------------------------------
    def toggleStatus(self, state):
        """"""
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    

if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())