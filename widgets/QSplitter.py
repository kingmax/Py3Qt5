#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/12
"""

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
        hbox = QHBoxLayout(self)
        
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        
        sp1 = QSplitter(Qt.Horizontal)
        sp1.addWidget(topleft)
        sp1.addWidget(topright)
        
        sp2 = QSplitter(Qt.Vertical)
        sp2.addWidget(sp1)
        sp2.addWidget(bottom)
        
        hbox.addWidget(sp2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())