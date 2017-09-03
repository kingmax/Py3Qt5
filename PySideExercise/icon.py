#coding:utf-8
#icon.py

import sys
from PySide import QtGui

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()