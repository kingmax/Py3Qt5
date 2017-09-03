#coding:utf-8
#label.py
#http://blog.csdn.net/a359680405/article/details/45096185

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("<p style='color: red; margin-left: 20px'> <b>hell world</b> </p>")
label.show()

sys.exit(app.exec_())