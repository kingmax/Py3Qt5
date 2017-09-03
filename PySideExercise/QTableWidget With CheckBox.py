#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: QTableWidget With CheckBox
  Created: 2016/8/22
"""

import unittest
import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.table = QtGui.QTableWidget(self)
        
        cell = QtGui.QWidget()
        checkBox = QtGui.QCheckBox()
        boxLayout = QtGui.QHBoxLayout(cell)
        boxLayout.addWidget(checkBox)
        boxLayout.setAlignment(QtCore.Qt.AlignCenter)
        boxLayout.setContentsMargins(0,0,0,0)
        cell.setLayout(boxLayout)
        
        self.table.setCellWidget(0, 0, cell)
        self.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    unittest.main()
    