#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/10
"""

import unittest

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

########################################################################
class Window(QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        super(Window, self).__init__()
        self.initUI()
        
    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        #self.setGeometry(300, 300, 250, 150)
        self.resize(300, 200)
        #self.center()
        
        btn = QPushButton('move2center', self)
        btn.clicked.connect(self.center)
        btn.move(10,20)
        
        self.setWindowTitle('Center')
        self.setWindowIcon(QIcon('D:\2017.6.6\li.jpg'))
        self.show()
        
    #----------------------------------------------------------------------
    def center(self):
        """"""
        win_rect = self.frameGeometry()
        the_center = QDesktopWidget().availableGeometry().center()
        win_rect.moveCenter(the_center)
        self.move(win_rect.topLeft())
    
    

if __name__ == '__main__':
    #unittest.main()
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())