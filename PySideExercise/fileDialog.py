#coding:utf-8
#fileDialog.py

import sys
from PySide import QtGui

class Win(QtGui.QMainWindow):
    def __init__(self):
        super(Win,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.te = QtGui.QTextEdit()
        self.setCentralWidget(self.te)
        self.statusBar()
        
        openFile = QtGui.QAction(QtGui.QIcon('icon.png'), '&Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)
        
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openFile)
        
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('File Dialog')
        self.show()
        
    def showDialog(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.te.setText(data)
        
            
            
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()