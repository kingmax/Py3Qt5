#coding:utf-8
#centerWin.py

import sys
from PySide import QtGui

class Win(QtGui.QWidget):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(250,150)
        self.center()
        
        self.setWindowTitle('Center')
        self.show()
        
    def center(self):
        rect = self.frameGeometry()
        centerPos = QtGui.QDesktopWidget().availableGeometry().center()
        rect.moveCenter(centerPos)
        #self.move(rect.topLeft())
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    