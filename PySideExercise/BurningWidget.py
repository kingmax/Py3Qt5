#coding:utf-8
#burningWidget.py

import sys
from PySide import QtGui, QtCore


class Communicate(QtCore.QObject):
    updateBW = QtCore.Signal(int)
    

class BurningWidget(QtGui.QWidget):
    def __init__(self):
        super(BurningWidget, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]
        
    def setValue(self, v):
        self.value = v
        
    def paintEvent(self, e):
        qb = QtGui.QPainter()
        qb.begin(self)
        self.drawWidget(qb)
        qb.end()
        
    def drawWidget(self, qb):
        font = QtGui.QFont('Tahoma', 7, QtGui.QFont.Light)
        qb.setFont(font)
        
        size = self.size()
        w = size.width()
        h = size.height()
        
        step = int(round(w / 10.0))
        
        till = int((w / 750.0) * self.value)
        full = int((w / 750.0) * 700)
        
        if self.value >= 700:
            qb.setPen(QtGui.QColor(255,255,255))
            qb.setBrush(QtGui.QColor(255,255,184))
            qb.drawRect(0, 0, full, h)
            qb.setPen(QtGui.QColor(255, 175, 175))
            qb.setBrush(QtGui.QColor(255, 175, 175))
            qb.drawRect(full, 0, till-full, h)
        else:
            qb.setPen(QtGui.QColor(255, 255, 255))
            qb.setBrush(QtGui.QColor(255, 255, 184))
            qb.drawRect(0, 0, till, h)
            
        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, QtCore.Qt.SolidLine)
        qb.setPen(pen)
        qb.setBrush(QtCore.Qt.NoBrush)
        qb.drawRect(0, 0, w-1, h-1)
        
        j = 0
        
        for i in range(step, 10*step, step):
            qb.drawLine(i, 0, i, 5)
            metrics = qb.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qb.drawText(i-fw/2, h/2, str(self.num[j]))
            j += 1
            
            
class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setRange(1, 750)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)
        
        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)
        sld.valueChanged[int].connect(self.changeValue)
        
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()
        
    def changeValue(self, v):
        self.c.updateBW.emit(v)
        self.wid.repaint()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    #w = BurningWidget()
    #w.show()    
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()