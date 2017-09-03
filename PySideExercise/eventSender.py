#coding:utf-8
#eventSender.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QMainWindow):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        btnA = QtGui.QPushButton('Button A', self)
        btnA.move(30, 50)
        
        btnB = QtGui.QPushButton('Button B', self)
        btnB.move(150, 50)
        
        btnA.clicked.connect(self.btnClicked)
        btnB.clicked.connect(self.btnClicked)
        
        self.statusBar()
        
        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Event sender')
        self.show()
        
    def btnClicked(self):
        sender = self.sender()
        print(sender)
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
        
    