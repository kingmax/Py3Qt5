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
        self.setAcceptDrops(True)
        
    #----------------------------------------------------------------------
    def dragEnterEvent(self, event):
        """"""
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            e.ignore()
            
    #----------------------------------------------------------------------
    def dropEvent(self, event):
        """"""
        print(event.mimeData())
        self.setText(event.mimeData().text())
    
    

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
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)
        
        btn = Button('Button', self)
        btn.move(190, 65)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple drag and drop')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())