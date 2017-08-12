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

        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Brushes')
        self.show()
        
    #----------------------------------------------------------------------
    def paintEvent(self, e):
        """"""
        pt = QPainter()
        pt.begin(self)
        self.drawBrushes(pt)
        pt.end()
        
    #----------------------------------------------------------------------
    def drawBrushes(self, pt):
        """"""
        pt.setPen(Qt.blue)
        brush = QBrush(Qt.SolidPattern)
        pt.setBrush(brush)
        pt.drawRect(10, 15, 90, 60)
        
        brush.setStyle(Qt.Dense1Pattern)
        pt.setBrush(brush)
        pt.drawRect(130, 15, 90, 60)
        
        brush.setStyle(Qt.Dense2Pattern)
        pt.setBrush(brush)
        pt.drawRect(250, 15, 90, 60)
        
        brush.setStyle(Qt.DiagCrossPattern)
        pt.setBrush(brush)
        pt.drawRect(10, 105, 90, 60)
        
        brush.setStyle(Qt.Dense6Pattern)
        pt.setBrush(brush)
        pt.drawRect(130, 105, 90, 60)
        
        brush.setStyle(Qt.Dense5Pattern)
        pt.setBrush(brush)
        pt.drawRect(250, 105, 90, 60)
        
        brush.setStyle(Qt.HorPattern)
        pt.setBrush(brush)
        pt.drawRect(10, 195, 90, 60)
        
        brush.setStyle(Qt.VerPattern)
        pt.setBrush(brush)
        pt.drawRect(130, 195, 90, 60)
        
        brush.setStyle(Qt.BDiagPattern)
        pt.setBrush(brush)
        pt.drawRect(250, 195, 90, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())