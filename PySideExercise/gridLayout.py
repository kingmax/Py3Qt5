#coding:utf-8
#gridLayout.py

import sys
from PySide import QtGui

class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        names = ['Cls', 'Bck',  '', 'Close',
                 '7',    '8',   '9', '/', 
                 '4',    '5',   '6', '*',
                 '1',    '2',   '3', '-',
                 '0',    '.',   '=', '+']
        
        grid = QtGui.QGridLayout()
        j = 0
        pos = [(0,0), (0,1), (0,2), (0,3),
               (1,0), (1,1), (1,2), (1,3),
               (2,0), (2,1), (2,2), (2,3),
               (3,0), (3,1), (3,2), (3,3),
               (4,0), (4,1), (4,2), (4,3)]
        for n in names:
            button = QtGui.QPushButton(n)
            if j == 2:
                grid.addWidget(QtGui.QLabel(''), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j += 1
        self.setLayout(grid)
        
        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()