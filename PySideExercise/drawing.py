#coding:utf-8
#drawing.py

import sys
from PySide import QtGui, QtCore


class Win(QtGui.QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.txt = self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'
        
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Draw text')
        self.show()
        
    def paintEvent(self, event):
        qb = QtGui.QPainter()
        qb.begin(self)
        
        #self.drawText(event, qb)
        qb.setPen(QtGui.QColor(168, 34, 3))
        qb.setFont(QtGui.QFont('Decorative', 10))
        qb.drawText(event.rect(), QtCore.Qt.AlignCenter, self.txt)
        
        qb.end()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()