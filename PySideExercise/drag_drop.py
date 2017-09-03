#coding:utf-8
#drag_drop.py

import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Button(QPushButton):
    def __init__(self):
        super(Button, self).__init__()
        
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
            
    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        

class Win(QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        le = QLineEdit('', self)
        le.setDragEnabled(True)
        le.move(30, 65)
        
        btn = Button('Button', self)
        btn.move(190, 65)
        
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Simple Drag & Drop')
        self.show()
        
        
def main():
    app = QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()