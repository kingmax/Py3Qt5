#!/usr/bin/env python
#-*- coding:utf-8 -*-

#---------
# IMPORT
#---------
from PySide import QtGui, QtCore

#---------
# MAIN
#---------
class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        numberRows    = 3
        numberColumns = 2

        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setRowCount(numberRows)
        self.tableWidget.setColumnCount(numberColumns)

        for rowNumber in range(numberRows):
            for columnNumber in range(numberColumns):    
                item = QtGui.QTableWidgetItem("item {0} {1}".format(rowNumber, columnNumber))
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Unchecked)

                self.tableWidget.setItem(rowNumber, columnNumber, item)

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableWidget)

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.resize(333, 111)
    main.show()

    sys.exit(app.exec_())