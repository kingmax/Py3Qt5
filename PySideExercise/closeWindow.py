#coding:utf-8
#closeWindow.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win,self).__init__()
        self.initUI()
        
    def initUI(self):
        btnQuit = QtGui.QPushButton('Quit', self)
        btnQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btnQuit.resize(btnQuit.sizeHint())
        btnQuit.move(50, 50)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Quit Button')
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()