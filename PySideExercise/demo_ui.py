# -*- coding: utf-8 -*-
#demo_ui.py

import sys
from PySide import QtGui, QtCore
from ui_submiter import Ui_Form

class Win(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)
        self.show()
   
def main():
    app = QtGui.QApplication(sys.argv)
    win = Win()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
