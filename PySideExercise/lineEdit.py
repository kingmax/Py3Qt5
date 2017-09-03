#coding:utf-8
#lineEdit.py

import sys
from PySide import QtGui, QtCore


class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QtGui.QLabel(self)
        le = QtGui.QLineEdit(self)
        
        le.move(60, 100)
        self.lbl.move(60, 40)
        
        le.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
        
    def onChanged(self, txt):
        self.lbl.setText(txt)
        self.lbl.adjustSize()
        

def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
        