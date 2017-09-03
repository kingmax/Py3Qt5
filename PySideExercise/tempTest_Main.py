#coding:utf-8
#tempTest_Main.py

import sys
from PySide import QtGui, QtCore
from tempTest import Ui_MainWindow


class Win(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.hi)
        
        self.show()
        
    @QtCore.Slot()
    def hi(self):
        sender = self.sender()
        print(sender)
        self.ui.statusbar.showMessage(sender.text())
        

def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    win.ui.statusbar.showMessage('ready')
    #win.hi()
    sys.exit(app.exec_())
 
    
if __name__ == '__main__':
    main()