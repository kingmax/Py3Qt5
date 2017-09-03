#coding:utf-8
#dialog_show.py

import sys
from PySide import QtGui, QtCore

import dialog

class Win(QtGui.QDialog, dialog.Ui_Dialog):
    def __init__(self, p=None):
        super(Win, self).__init__(p)
        self.setupUi(self)
        self.setLayout(self.horizontalLayout)
        self.pushButton.clicked.connect(self.showMessageBox)
        self.show()
        
    def showMessageBox(self):
        QtGui.QMessageBox.information(self, 'hello', 'hello there, %s'%self.lineEdit.text())
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())