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
class Button(QPushButton):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, title, parent):
        """Constructor"""
        
        super(Button, self).__init__(title, parent)
        
    #----------------------------------------------------------------------
    def mouseMoveEvent(self, e):
        """"""
        if e.buttons() != Qt.RightButton:
            return
        
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        drag.exec_(Qt.MoveAction)
        
    #----------------------------------------------------------------------
    def mousePressEvent(self, e):
        """"""
        super(Button, self).mousePressEvent(e)
        
        if e.button() == Qt.LeftButton:
            print('press')
    

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
        self.setAcceptDrops(True)
        
        self.button = Button('Button', self)
        self.button.move(100, 65)
        

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Click or Move button')
        self.show()
        
    #----------------------------------------------------------------------
    def dragEnterEvent(self, e):
        """"""
        e.accept()
        
    #----------------------------------------------------------------------
    def dropEvent(self, e):
        """"""
        pos = e.pos()
        self.button.move(pos)
        
        #e.setDropAction(Qt.MoveAction)
        #e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())