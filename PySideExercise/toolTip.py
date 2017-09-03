#coding:utf-8
#tooltip.py

import sys
from PySide import QtGui

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Tooltips')
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
        