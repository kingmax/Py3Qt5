#coding:utf-8
#point.py

import sys, random
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()
        
    def paintEvent(self, event):
        qb = QtGui.QPainter()
        qb.begin(self)
        self.drawPoints(qb)
        qb.end()
        
    def drawPoints(self, qb):
        qb.setPen(QtCore.Qt.red)
        size = self.size()
        
        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qb.drawPoint(x, y)
            
            
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()