#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/11
"""

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
        vbox = QtWidgets.QVBoxLayout()
        
        btn = QtWidgets.QPushButton('set Font', self)
        btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        btn.move(20, 10)
        btn.clicked.connect(self.setFont)
        vbox.addWidget(btn)
        
        self.lbl = QtWidgets.QLabel('Knowledge only matters', self)
        self.lbl.move(120, 20)
        vbox.addWidget(self.lbl)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
        
    #----------------------------------------------------------------------
    def setFont(self):
        """"""
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())