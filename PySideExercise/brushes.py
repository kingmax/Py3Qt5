#coding:utf-8
#brushes.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()
        
    def paintEvent(self, e):
        qb = QtGui.QPainter()
        qb.begin(self)
        self.drawBrushes(qb)
        qb.end()
        
    def drawBrushes(self, qb):
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        qb.setBrush(brush)
        qb.drawRect(10, 15, 90, 60)
        
        brush.setStyle(QtCore.Qt.Dense1Pattern)
        qb.setBrush(brush)
        qb.drawRect(130, 15, 90, 60)
        
        brush.setStyle(QtCore.Qt.Dense2Pattern)
        qb.setBrush(brush)
        qb.drawRect(250, 15, 90, 60)
        
        
        brush.setStyle(QtCore.Qt.Dense3Pattern)
        qb.setBrush(brush)
        qb.drawRect(10, 105, 90, 60)
        
        brush.setStyle(QtCore.Qt.DiagCrossPattern)
        qb.setBrush(brush)
        qb.drawRect(130, 105, 90, 60)
        
        brush.setStyle(QtCore.Qt.Dense5Pattern)
        qb.setBrush(brush)
        qb.drawRect(250, 105, 90, 60)
        
        brush.setStyle(QtCore.Qt.HorPattern)
        qb.setBrush(brush)
        qb.drawRect(10, 195, 90, 60)
        
        brush.setStyle(QtCore.Qt.VerPattern)
        qb.setBrush(brush)
        qb.drawRect(130, 195, 90, 60)
        
        brush.setStyle(QtCore.Qt.BDiagPattern)
        qb.setBrush(brush)
        qb.drawRect(250, 195, 90, 60)
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()