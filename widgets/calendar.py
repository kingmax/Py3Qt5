#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/11
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
        vbox = QtWidgets.QVBoxLayout(self)
        
        cal = QtWidgets.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        
        vbox.addWidget(cal)
        
        self.lbl = QtWidgets.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        
        vbox.addWidget(self.lbl)
        
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
        
    #----------------------------------------------------------------------
    def showDate(self, date):
        """"""
        self.lbl.setText(date.toString())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())