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
        self.setWindowTitle('Context menu')
        self.show()
        
    #----------------------------------------------------------------------
    def contextMenuEvent(self, event):
        """override contexMenuEvent"""
        cmenu = QtWidgets.QMenu(self)
        
        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAct:
            QtWidgets.qApp.quit()
            

if __name__ == '__main__':
    #unittest.main()
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())