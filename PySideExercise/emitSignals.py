#coding:utf-8
#emittingSignals.py

import sys
from PySide import QtGui, QtCore

class Communicate(QtCore.QObject):
    closeApp = QtCore.Signal()
    
class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        
        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    def mousePressEvent(self, e):
        self.c.closeApp.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()