# -*- coding: utf-8 -*-

#http://wiki.qt.io/QtCreator_and_PySide


# Form implementation generated from reading ui file 'D:\CloudRenderFarm\Plugins\Houdini\PySideExercise\mainWindow.ui'
#
# Created: Fri Jul 29 14:05:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 70, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Fele = QtGui.QMenu(self.menubar)
        self.menu_Fele.setObjectName("menu_Fele")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        
        self.action_Exit.triggered.connect(MainWindow.close)
        
        self.menu_Fele.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_Fele.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Hello, World!", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Fele.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Exit Application", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))


'''
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
'''