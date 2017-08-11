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
        self.icons = [QtGui.QPixmap('mute.png'), QtGui.QPixmap('min.png'), QtGui.QPixmap('med.png'), QtGui.QPixmap('max.png'),]
        
        sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(20, 20, 260, 20)
        sld.valueChanged[int].connect(self.changeValue)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setPixmap(self.icons[0])
        self.label.setGeometry(40, 20, 255, 255)
        
        self.setGeometry(300, 300, 300, 260)
        self.setWindowTitle('Slider')
        self.show()
        
    #----------------------------------------------------------------------
    def changeValue(self, val):
        """"""
        if val == 0:
            self.label.setPixmap(self.icons[0])
        elif val > 0 and val <=30:
            self.label.setPixmap(self.icons[1])
        elif val > 30 and val <= 80:
            self.label.setPixmap(self.icons[2])
        else:
            self.label.setPixmap(self.icons[-1])



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())