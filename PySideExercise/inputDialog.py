#coding:utf-8
#inputDialog.py

import sys
from PySide import QtGui

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        btn = QtGui.QPushButton('Dialog', self)
        btn.move(20,20)
        btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(100, 22)
        
        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input Dialog')
        self.show()
        
    def showDialog(self):
        txt, ok = QtGui.QInputDialog.getText(self, 'Query', 'Enter your name:')
        if ok:
            self.le.setText(str(txt))
            
            
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
    