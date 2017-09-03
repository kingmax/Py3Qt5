#coding:utf-8
#colorDialog.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QMainWindow):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        col = QtGui.QColor(0,0,0)
        btn = QtGui.QPushButton('Dialog', self)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)
        
        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet('QWidget {background-color:%s}'%col.name())
        self.frm.setGeometry(130,22,100,100)
        
        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Color dialog')
        self.show()
        
    def showDialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet('QWidget{background-color:%s}'%col.name())
            
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()