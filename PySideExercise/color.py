#coding:utf-8
#color.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colors')
        self.show()
        
    def paintEvent(self, e):
        qb = QtGui.QPainter()
        qb.begin(self)
        self.drawRectangles(qb)
        qb.end()
        
    def drawRectangles(self, qb):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qb.setPen(color)
        
        qb.setBrush(QtGui.QColor(200, 0, 0))
        qb.drawRect(10, 15, 90, 60)
        
        qb.setBrush(QtGui.QColor(255, 80, 0, 160))
        qb.drawRect(130, 15, 90, 60)
        
        qb.setBrush(QtGui.QColor(25, 0, 90, 200))
        qb.drawRect(250, 15, 90, 60)
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
        