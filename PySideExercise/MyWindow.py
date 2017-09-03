#!/usr/bin/env python
#coding:utf-8
"""
  Author:  kingmax_res@163.com --<184327932@qq.com>
  Purpose: 
  Created: 2016/10/9
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.resize(700,400)
        self.setMinimumSize(600, 300)
        self.setWindowTitle('HPRender')
        
        self.grid = QGridLayout(self)
        
        self.gb1 = QGroupBox(self)
        self.hbox = QHBoxLayout(self.gb1)
        self.label = QLabel('Name:', self.gb1)
        self.hbox.addWidget(self.label)
        self.sceneName = QLineEdit(self.gb1)
        self.hbox.addWidget(self.sceneName)
        self.grid.addWidget(self.gb1, 0, 0, 1, 1)
        
        self.gbTask = QGroupBox(self)
        self.model = QStandardItemModel(4, 7)
        headers = ['ROP', 'Camera', 'Take', 'Range', 'Resolution', 'Preview', 'Output']
        self.model.setHorizontalHeaderLabels(headers)    
        self.taskTable = QTableView(self.gbTask)
        self.taskTable.setModel(self.model)
        self.taskTable.verticalHeader().setVisible(False)
        
        self.hbox2 = QHBoxLayout(self.gbTask)
        self.btnSelAll = QPushButton('sel All', self.gbTask)
        self.btnSelInvert = QPushButton('sel Invert', self.gbTask)
        self.chkAutoDownload = QCheckBox('Auto Download', self.gbTask)
        self.chkAutoDownload.setChecked(True)
        self.chkContinue = QCheckBox('Continue After 10 mins', self.gbTask)
        self.hbox2.addWidget(self.btnSelAll)
        self.hbox2.addWidget(self.btnSelInvert)
        self.hbox2.addWidget(self.chkAutoDownload)
        self.hbox2.addWidget(self.chkContinue)
        
        self.vboxTask = QVBoxLayout(self.gbTask)
        self.vboxTask.addWidget(self.taskTable)
        self.vboxTask.addLayout(self.hbox2)
        self.grid.addWidget(self.gbTask, 1, 0, 1, 1)
               
        self.gb2 = QGroupBox(self)
        self.hbox3 = QHBoxLayout(self.gb2)
        self.btnRetry = QPushButton('Retry', self.gb2)
        self.btnSubmit = QPushButton('Submit', self.gb2)
        self.hbox3.addWidget(self.btnRetry)
        self.hbox3.addWidget(self.btnSubmit)
        #self.vbox.addLayout(self.hbox3)
        self.grid.addWidget(self.gb2, 2, 0, 2, 1)
        
        self.logList = QListView(self)
        #self.logList.setMaximumHeight(100)
        self.grid.addWidget(self.logList, 5, 0, 1, 1)
        
       
        
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())