#coding:utf-8
#dragButton.py

import sys
from PySide import QtGui, QtCore


class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        
    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return
        
        mimeData = QtCore.QMimeData()
        
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        
        dropAction = drag.start(QtCore.Qt.MoveAction)
        
    def mousePressEvent(self, e):
        super(Button, self).mousePressEvent(e)
        if e.buttons() == QtCore.Qt.LeftButton:
            print('Pressed')

            
class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setAcceptDrops(True)
        
        self.btn = Button('Button', self)
        self.btn.move(100, 65)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Click or Move')
        self.show()
        
    def dragEnterEvent(self, e):
        e.accept()
        
    def dropEvent(self, e):
        pos = e.pos()
        self.btn.move(pos)
        
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
