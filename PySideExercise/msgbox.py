#coding:utf-8
#msgbox.py

import sys
from PySide import QtGui

class Win(QtGui.QWidget):
    
    def __init__(self):
        super(Win,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message Box')
        self.show()
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self,'Message','Are you sure to quit?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()