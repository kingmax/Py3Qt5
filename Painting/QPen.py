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
        

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen style')
        self.show()
        
    #----------------------------------------------------------------------
    def paintEvent(self, e):
        """"""
        pt = QPainter()
        pt.begin(self)
        self.drawLines(pt)
        pt.end()
        
    #----------------------------------------------------------------------
    def drawLines(self, pt):
        """"""
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        pt.setPen(pen)
        pt.drawLine(20, 40, 250, 40)
        
        pen.setStyle(Qt.DashLine)
        pt.setPen(pen)
        pt.drawLine(20, 80, 250, 80)
        
        pen.setStyle(Qt.DashDotLine)
        pt.setPen(pen)
        pt.drawLine(20, 120, 250, 120)
        
        pen.setStyle(Qt.DotLine)
        pt.setPen(pen)
        pt.drawLine(20, 160, 250, 160)
        
        pen.setStyle(Qt.DashDotDotLine)
        pt.setPen(pen)
        pt.drawLine(20, 200, 250, 200)
        
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        pt.setPen(pen)
        pt.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())