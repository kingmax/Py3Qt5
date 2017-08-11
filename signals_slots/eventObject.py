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
        grid = QtWidgets.QGridLayout(self)
        grid.setSpacing(10)
        
        x = 0
        y = 0
        txt = "x: {0}, y: {1}".format(x, y)
        self.label = QtWidgets.QLabel(txt, self)
        grid.addWidget(self.label, 0, 0, QtCore.Qt.AlignTop)
        
        self.setMouseTracking(True)
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Event object')
        self.show()
        
    #----------------------------------------------------------------------
    def mouseMoveEvent(self, event):
        """"""
        x = event.x()
        y = event.y()
        self.label.setText('x: {0}, y:{1}'.format(x, y))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())