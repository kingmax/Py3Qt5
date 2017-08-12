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
        self.setStyleSheet('QMainWindow{background-color:gray}')

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()
        
    #----------------------------------------------------------------------
    def paintEvent(self, e):
        """"""
        pt = QPainter()
        pt.begin(self)
        self.drawRectangle(pt)
        pt.end()
        
    #----------------------------------------------------------------------
    def drawRectangle(self, painter):
        """"""
        col = QColor(0, 0, 0)
        #col.setNamedColor('#d4d4d4')
        painter.setPen(col)
        
        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(10, 15, 90, 60)
        
        painter.setBrush(QColor(255, 80, 0, 160))
        painter.drawRect(130, 15, 90, 60)
        
        painter.setBrush(QColor(25, 0, 90, 200))
        painter.drawRect(250, 15, 90, 60)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())