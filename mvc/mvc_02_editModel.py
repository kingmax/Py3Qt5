#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: edit, delete, add data from any views
  Ref:     https://blog.rburchell.com/2010/02/pyside-tutorial-model-view-programming_22.html
  Created: 2017/10/15
"""

import sys
from PySide.QtCore import *
from PySide.QtGui import *

#Model
########################################################################
class SimpleListModel(QAbstractListModel):
    """Model"""

    #----------------------------------------------------------------------
    def __init__(self, mlist):
        """Constructor"""
        super(SimpleListModel, self).__init__()
        self._items = mlist
        
    #----------------------------------------------------------------------
    def rowCount(self, parent=QModelIndex()):
        """how many rows in data"""
        return len(self._items)
    
    #----------------------------------------------------------------------
    def data(self, index, role=Qt.DisplayRole):
        """"""
        if role == Qt.DisplayRole:
            return self._items[index.row()]
        elif role == Qt.EditRole:
            return self._items[index.row()]
        else:
            return None
        
    #----------------------------------------------------------------------
    def setData(self, index, value, role=Qt.EditRole):
        """"""
        if role == Qt.EditRole:
            self._items[index.row()] = str(value.toString().toUtf8())
            self.dataChanged.emit(index, index) #always emit the dataChanged, so views know need to update
            return True
        return False
    
    #----------------------------------------------------------------------
    def flags(self, index):
        """set item selectable, draggable..."""
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
    
    #----------------------------------------------------------------------
    def removeRows(self, row, count, parent=QModelIndex()):
        """row is the row number to be removed
        count are the total number of rows to remove
        parent is pretty much of relevant for tree model"""
        if row < 0 or row > len(self._items):
            return
        
        self.beginRemoveRows(parent, row, row + count - 1)
        while count != 0:
            del self._items[row]
            count -= 1
        self.endRemoveRows()
        
    #----------------------------------------------------------------------
    def addItem(self, item):
        """"""
        self.beginInsertRows(QModelIndex(), len(self._items), len(self._items))
        self._items.append(str(item))
        self.endInsertRows()
        
        
#View
########################################################################
class SimpleListView(QListView):
    """View"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        super(SimpleListView, self).__init__()
        self.setAlternatingRowColors(True)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        
        a = QAction('Delete Selected', self)
        a.triggered.connect(self.onTriggered)
        self.addAction(a)
        
    #----------------------------------------------------------------------
    def onTriggered(self):
        """"""
        self.model().removeRows(self.currentIndex().row(), 1)
        
        
#Application
########################################################################
class MainWindow(QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(MainWindow, self).__init__()
        self.setWindowTitle('Editable Model')
        
        self._model = SimpleListModel(['a', 'b', 'c', 'd', 'e'])
        
        vbox = QVBoxLayout()
        
        v1 = SimpleListView()
        v1.setModel(self._model)
        vbox.addWidget(v1)
        
        v2 = SimpleListView()
        v2.setModel(self._model)
        vbox.addWidget(v2)
        
        hbox = QHBoxLayout()
        
        self._itemedit = QLineEdit()
        b = QPushButton('Add Item')
        b.clicked.connect(self.doAddItem)
        hbox.addWidget(self._itemedit)
        hbox.addWidget(b)
        
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
    #----------------------------------------------------------------------
    def doAddItem(self):
        """"""
        self._model.addItem(self._itemedit.text())
        self._itemedit.setText('')
        
#Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
        
        
    
    
    
    
        
    
    
        
    
