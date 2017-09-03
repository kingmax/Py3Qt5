#coding:utf-8
#simple.py

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

wind = QtGui.QWidget()
wind.resize(250, 150)
wind.setWindowTitle('Simple')
wind.show()

sys.exit(app.exec_())