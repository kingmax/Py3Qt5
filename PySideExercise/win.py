#coding:utf-8
#win.py
#http://blog.csdn.net/a359680405/article/details/45096185

import sys
from PySide import QtGui


class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        

def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    label = QtGui.QLabel(win)
    label.setText('Hello, World.')
    win.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()