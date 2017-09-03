# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp.ui'
#
# Created: Tue Aug 02 23:03:20 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 305)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

