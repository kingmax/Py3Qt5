#coding:utf-8
#splitter.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QtGui.QHBoxLayout()

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)
        
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)
        
        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        #splitter2.resize(splitter2.width(), 100)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Splitter')
        self.show()
        

def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()