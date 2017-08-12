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
        self.setStyleSheet('QMainWindow{background-color:black}')

        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Bezier curve')
        self.show()
        
    #----------------------------------------------------------------------
    def paintEvent(self, e):
        """"""
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(pt)
        pt.end()
        
    #----------------------------------------------------------------------
    def drawBezierCurve(self, pt):
        """"""
        pt.setPen(Qt.blue)
        
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)
        path.cubicTo(350, 30, 200, 150, 350, 270)
        
        pt.drawPath(path)
        
    #----------------------------------------------------------------------
    def mouseMoveEvent(self, e):
        """"""
        print(e.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())