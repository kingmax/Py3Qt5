#coding:utf-8
#toolbar.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QMainWindow):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('icon.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setToolTip('close application')
        exitAction.setStatusTip('Close Application')
        exitAction.triggered.connect(self.close)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.statusBar()
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Toolbar')
        
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()