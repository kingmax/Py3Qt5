#coding:utf-8
#pen.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()
        
    def paintEvent(self, e):
        qb = QtGui.QPainter()
        qb.begin(self)
        self.drawLines(qb)
        qb.end()
        
    def drawLines(self, qb):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        
        qb.setPen(pen)
        qb.drawLine(20, 40, 250, 40)
        
        pen.setStyle(QtCore.Qt.DashLine)
        qb.setPen(pen)
        qb.drawLine(20, 80, 250, 80)
        
        pen.setStyle(QtCore.Qt.DashDotLine)
        qb.setPen(pen)
        qb.drawLine(20, 120, 250, 120)
        
        pen.setStyle(QtCore.Qt.DotLine)
        qb.setPen(pen)
        qb.drawLine(20, 160, 250, 160)
        
        pen.setStyle(QtCore.Qt.DashDotDotLine)
        qb.setPen(pen)
        qb.drawLine(20, 200, 250, 200)
        
        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 8, 4])
        qb.setPen(pen)
        qb.drawLine(20, 240, 250, 240)
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()