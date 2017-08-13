#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/13
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

########################################################################
class Communicate(QObject):
    """"""
    updateBW = pyqtSignal(int)
    
########################################################################
class BurningWidget(QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        super(BurningWidget, self).__init__()
        self.initUI()
        
    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]
        
    #----------------------------------------------------------------------
    def setValue(self, val):
        """"""
        self.value = val
        
    #----------------------------------------------------------------------
    def paintEvent(self, e):
        """"""
        pt = QPainter()
        pt.begin(self)
        self.drawWidget(pt)
        pt.end()
        
    #----------------------------------------------------------------------
    def drawWidget(self, pt):
        """"""
        MAX_CAPACITY  = 700
        OVER_CAPACITY = 750
        
        font = QFont('Serif', 7, QFont.Light)
        pt.setFont(font)
        
        size = self.size()
        w = size.width()
        h = size.height()
        step = int(round(w/10))
        till = int((w / OVER_CAPACITY) * self.value)
        full = int((w / OVER_CAPACITY) * MAX_CAPACITY)
        
        pt.setPen(Qt.white)
        pt.setBrush(QColor(255, 255, 184))  
        if self.value >= MAX_CAPACITY:
            pt.drawRect(0, 0, full, h)
            c = QColor(255, 175, 175)
            pt.setPen(c)
            pt.setBrush(c)
            pt.drawRect(full, 0, till-full, h)
        else:
            pt.drawRect(0, 0, till, h)
            
        pen = QPen(QColor(20, 20, 20), 1, Qt.SolidLine)
        pt.setPen(pen)
        pt.setBrush(Qt.NoBrush)
        pt.drawRect(0, 0, w-1, h-1)
        
        j = 0
        for i in range(step, 10*step, step):
            pt.drawLine(i, 0, i, 5)
            metrics = pt.fontMetrics()
            txt = str(self.num[j])
            fw = metrics.width(txt)
            pt.drawText(i-fw/2, h/2, txt)
            j += 1
    

########################################################################
class Window(QWidget):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Window, self).__init__()
        self.initUI()

    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        OVER_CAPACITY = 750
        
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, OVER_CAPACITY)
        sld.setValue(75)
        sld.setGeometry(30, 40, 300, 30)
        
        self.c = Communicate()
        self.bwWidget = BurningWidget()
        self.c.updateBW[int].connect(self.bwWidget.setValue)
        
        sld.valueChanged[int].connect(self.changeValue)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.bwWidget)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Customize Burning Widget')
        self.show()
        
    #----------------------------------------------------------------------
    def changeValue(self, val):
        """"""
        self.c.updateBW.emit(val)
        self.bwWidget.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())