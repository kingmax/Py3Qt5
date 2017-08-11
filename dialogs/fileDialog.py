#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/11
"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

########################################################################
class Window(QtWidgets.QMainWindow):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        super(Window, self).__init__()
        self.initUI()

    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openAct = QtWidgets.QAction(QtGui.QIcon(r'D:\2017.6.6\li.jpg'), '&Open', self)
        openAct.setShortcut('Ctrl+o')
        openAct.setStatusTip('Open new file..')
        openAct.triggered.connect(self.openFile)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('MyWindow')
        self.show()
        
    #----------------------------------------------------------------------
    def openFile(self):
        """"""
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(filename) #('D:/cmd_temp.log', 'All Files (*)')
        if filename[0]:
            with open(filename[0]) as f:
                self.textEdit.setText(f.read())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())