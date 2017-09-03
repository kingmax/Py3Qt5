#coding:utf-8
#mainWindow.py
#http://wiki.qt.io/QtCreator_and_PySide

import sys
from PySide import QtGui, QtCore
from Ui_MainWindow import Ui_MainWindow


class Win(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()