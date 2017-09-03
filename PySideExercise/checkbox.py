#coding:utf-8
#checkbox.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QMainWindow):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('checkbox')
        self.show()
        
    def changeTitle(self, state):
        print(state)
        if state:
            self.setWindowTitle('Checkbox')
        else:
            self.setWindowTitle('')
            
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()