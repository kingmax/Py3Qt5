#coding:utf-8
#checkbutton.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QMainWindow):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.col = QtGui.QColor(0,0,0)
        
        rBtn = QtGui.QPushButton('Red', self)
        rBtn.setCheckable(True)
        rBtn.move(10,10)
        rBtn.clicked[bool].connect(self.setColor)
        
        gBtn = QtGui.QPushButton('Green', self)
        gBtn.setCheckable(True)
        gBtn.move(10,60)
        gBtn.clicked[bool].connect(self.setColor)
        
        bBtn = QtGui.QPushButton('Blue', self)
        bBtn.setCheckable(True)
        bBtn.move(10,110)
        bBtn.clicked[bool].connect(self.setColor)
        
        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget{background-color:%s}'%self.col.name())
        
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('checkbutton')
        self.show()
        
    def setColor(self, pressed):
        sender = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
            
        if sender.text() == 'Red':
            self.col.setRed(val)
        elif sender.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
            
        self.square.setStyleSheet('QFrame {background-color:%s}'%self.col.name())
        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()