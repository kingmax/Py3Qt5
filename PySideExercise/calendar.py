#coding:utf-8
#calendar.py

import sys
from PySide import QtGui, QtCore

class Win(QtGui.QWidget):
    
    def __init__(self):
        super(Win, self).__init__()
        self.initUI()
        
    def initUI(self):
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20,20)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        
        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)
        
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('calendar')
        self.show()
        
    def showDate(self, date):
        self.lbl.setText(date.toString())
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()