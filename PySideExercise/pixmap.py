#coding:utf-8
#pixmap.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QtGui.QHBoxLayout()
        pixmap = QtGui.QPixmap('icon.png')
        
        lbl = QtGui.QLabel()
        lbl.setPixmap(pixmap)
        
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Pixmap')
        self.show()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()