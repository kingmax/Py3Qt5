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
        col = QtGui.QColor(0,0,0)
        
        self.btn = QtWidgets.QPushButton('Pick Color', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.pickColorDialog)
        
        self.frm = QtWidgets.QFrame(self)
        self.frm.setStyleSheet('QWidget{background-color:%s}'%col.name())
        self.frm.setGeometry(130, 22, 100, 100)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('MyWindow')
        self.show()
        
    #----------------------------------------------------------------------
    def pickColorDialog(self):
        """"""
        col = QtWidgets.QColorDialog.getColor()
        
        if col.isValid():
            self.frm.setStyleSheet('QWidget{background-color:%s}'%col.name())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())