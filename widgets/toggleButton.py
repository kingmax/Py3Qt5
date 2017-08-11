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
        self.col = QtGui.QColor(0, 0, 0)
        
        btnR = QtWidgets.QPushButton('Red', self)
        btnR.setCheckable(True)
        btnR.move(10, 10)
        btnR.clicked[bool].connect(self.setColor)
        
        btnG = QtWidgets.QPushButton('Green', self)
        btnG.setCheckable(True)
        btnG.move(10, 60)
        btnG.clicked[bool].connect(self.setColor)      
        
        btnB = QtWidgets.QPushButton('Blue', self)
        btnB.setCheckable(True)
        btnB.move(10, 110)
        btnB.clicked[bool].connect(self.setColor)        
        
        self.square = QtWidgets.QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget {background-color:%s}'%self.col.name())
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toggle button')
        self.show()
        
    #----------------------------------------------------------------------
    def setColor(self, pressed):
        """"""
        sender = self.sender()
        
        val = 0
        if pressed:
            val = 255
        
        txt = sender.text()
        print(txt)
        if txt == 'Red':
            self.col.setRed(val)
        elif txt == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
            
        self.square.setStyleSheet('QFrame {background-color:%s}'%self.col.name())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())