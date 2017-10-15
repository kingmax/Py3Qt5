#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Ref:     https://blog.rburchell.com/2010/02/pyside-tutorial-model-view-programming.html
  Created: 2017/10/14
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys


# Model (data)
########################################################################
class SimpleListModel(QAbstractListModel):
    """Model"""

    #----------------------------------------------------------------------
    def __init__(self, mlist):
        """Constructor"""
        super(SimpleListModel, self).__init__()
        self._items = mlist #cache the passed data list as a class member
        
    #----------------------------------------------------------------------
    def rowCount(self, parent=QModelIndex()):
        """need to tell the view how many rows we have present in out data"""
        return len(self._items)
    
    #----------------------------------------------------------------------
    def data(self, index, role=Qt.DisplayRole):
        """the view request data info"""
        if not index.isValid():
            return None
        
        row = index.row()
        if role == Qt.DisplayRole:
            return self._items[row]
        elif role == Qt.BackgroundRole: #background decoration
            if row % 2 == 0:
                return QColor(Qt.gray)
            else:
                return QColor(Qt.lightGray)
            
        return None

        
#View (UI)
########################################################################
class SimpleListView(QListView):
    """View"""

    #----------------------------------------------------------------------
    def __init__(self, parent=None):
        """Constructor"""
        super(SimpleListView, self).__init__()
        
    
    
#App
########################################################################
class MainWindow(QWidget):
    """main app"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(MainWindow, self).__init__()
        self.setWindowTitle('Read-only Model')
        
        m = SimpleListModel(['a', 'b', 'c', 'd', 'e']) #data source (Model)
        
        vbox = QVBoxLayout()
        
        v1 = SimpleListView() #ui1 (View)
        v1.setModel(m)
        vbox.addWidget(v1)
        
        v2 = SimpleListView() #ui2 (View)
        v2.setModel(m)
        vbox.addWidget(v2)
        
        #hbox = QHBoxLayout()
        #vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        
#Main        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    
    
    
    