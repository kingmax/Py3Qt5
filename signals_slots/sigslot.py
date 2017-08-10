#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/10
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

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
        lcd = QtWidgets.QLCDNumber(self)
        sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        
        self.setLayout(vbox)
        
        sld.valueChanged.connect(lcd.display)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Signal and Slot')
        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())