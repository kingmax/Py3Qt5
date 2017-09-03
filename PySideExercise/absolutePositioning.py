#coding:utf-8
#absolutePositioning.py

import sys
from PySide import QtGui

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        labelA = QtGui.QLabel('Zetcode', self)
        labelA.move(15, 10)
        
        labelB = QtGui.QLabel('tutorials', self)
        labelB.move(35, 40)
        
        labelC = QtGui.QLabel('for programmers', self)
        labelC.move(55, 70)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute Positioning')
        self.show()
            
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()