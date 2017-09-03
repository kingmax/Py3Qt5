#coding:utf-8
#menubar.py

import sys
from PySide import QtGui, QtCore


class Win(QtGui.QMainWindow):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('icon.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Menubar')
        self.centralWidget()
        self.show()

        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()