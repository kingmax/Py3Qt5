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
        title = QtWidgets.QLabel('Title')
        author = QtWidgets.QLabel('Author')
        review = QtWidgets.QLabel('Review')
        
        txtTitle = QtWidgets.QLineEdit()
        txtAuthor = QtWidgets.QLineEdit()
        txtReview = QtWidgets.QTextEdit()
        
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        
        grid.addWidget(title, 1, 0)
        grid.addWidget(txtTitle, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(txtAuthor, 2, 1)
        grid.addWidget(review, 3, 0)
        
        #span 5 rows 1 column
        grid.addWidget(txtReview, 3, 1, 5, 1)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('ReviewZ')
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())