#coding:utf-8
#progressbar.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QMainWindow):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        
        self.btn = QtGui.QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        
        self.btnReset = QtGui.QPushButton('Reset', self)
        self.btnReset.move(150,80)
        self.btnReset.clicked.connect(self.reset)
        
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('progressbar')
        self.show()
        
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step += 1
        self.pbar.setValue(self.step)
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
    def reset(self):
        self.step = 0
        self.pbar.setValue(0)
        self.btn.setText('Start')
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()