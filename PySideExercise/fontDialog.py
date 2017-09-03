#coding:utf-8
#fontDialog.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QMainWindow):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        vbox = QtGui.QVBoxLayout()
        
        btn = QtGui.QPushButton('Dialog', self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)
        
        self.lbl = QtGui.QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
        
        vbox.addWidget(btn)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('FontDialog')
        self.show()
        
    def showDialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
            
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()