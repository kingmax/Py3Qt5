#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/12
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
        hbox = QtWidgets.QHBoxLayout(self)
        pixmap = QtGui.QPixmap('max.png')
        
        lbl = QtWidgets.QLabel(self)
        lbl.setGeometry(20, 20, 255, 255)
        lbl.setPixmap(pixmap)
        
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 300)
        self.move(300,300)
        self.setWindowTitle('Pixmap')
        self.show()
        
    #----------------------------------------------------------------------
    def keyPressEvent(self, event):
        """"""
        print(event)
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())