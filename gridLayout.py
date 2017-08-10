#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/10
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

########################################################################
class Window(QtWidgets.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        super(Window, self).__init__()
        self.initUI()

    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        names = ['Cls', 'Bck', '', 'Close', 
                 '7',   '8',   '9', '/', 
                 '4',   '5',   '6', '*', 
                 '1',   '2',   '3', '-', 
                 '0',   '.',   '=', '+']
        poses = [(i, j) for i in range(5) for j in range(4)]
        
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)
        
        for pos, name in zip(poses, names):
            #print(pos, name)
            if '' == name:
                continue
            
            btn = QtWidgets.QPushButton(name)
            grid.addWidget(btn, *pos)
        
        self.setGeometry(300, 200, 300, 200)
        self.setWindowTitle('Grid Layout')
        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())