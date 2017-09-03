#coding:utf-8
#comboBox.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QtGui.QLabel('Ubuntu', self)
        
        combo = QtGui.QComboBox(self)
        combo.addItems(['Ubuntu', 'Mandriva', 'Fedora', 'RedHat', 'Gentoo'])
        
        combo.move(50,50)
        self.lbl.move(50, 150)
        
        combo.activated[str].connect(self.onActivated)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('ComboBox')
        self.show()
        
    def onActivated(self, txt):
        self.lbl.setText(txt)
        self.lbl.adjustSize()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()