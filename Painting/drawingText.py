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
        self.text = "你好， PyQt5"

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Drawing text')
        self.show()
        
    #----------------------------------------------------------------------
    def paintEvent(self, e):
        """"""
        pt = QPainter()
        pt.begin(self)
        self.drawText(e, pt)
        pt.end()
        
    #----------------------------------------------------------------------
    def drawText(self, e, painter):
        """"""
        painter.setPen(QColor(168, 34, 3))
        painter.setFont(QFont('Decorative', 10))
        painter.drawText(e.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())