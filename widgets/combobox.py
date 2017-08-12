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
class Window(QMainWindow):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Window, self).__init__()
        self.initUI()

    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        self.lbl = QLabel('Ubuntu', self)
        
        combo = QComboBox(self)
        combo.addItems(['Ubuntu', 'Mandriva', 'Fedora', 'Arch', 'Gentoo'])
        combo.move(50,50)
        self.lbl.move(50, 150)
        
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()
        
    #----------------------------------------------------------------------
    def onActivated(self, txt):
        """"""
        self.lbl.setText(txt)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())