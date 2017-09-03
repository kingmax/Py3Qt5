#coding:utf-8
#slider.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.valueChanged[int].connect(self.changeValue)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('slider')
        self.show()
        
    def changeValue(self, val):
        print(val)
        self.lcd.display(val)
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()