#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: 2016/10/27
"""

import unittest

from PySide import QtGui, QtCore
import sys

data = [[1,2,3,4,5],[10,20,30,40,50]]

app = QtGui.QApplication(sys.argv)

########################################################################
class MyTable(QtCore.QAbstractTableModel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, data):
        """Constructor"""     
        super(MyTable, self).__init__()
        self._data = data
        
    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self._data)
    
    def columnCount(self, index=QtCore.QModelIndex()):
        return len(self._data[0])
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            #return 'xxx'
            return self._data[index.row()][index.column()]
        
table = MyTable(data)
view = QtGui.QTableView()
view.setMinimumSize(550, 200)
view.setModel(table)

view.show()
sys.exit(app.exec_())
    
    
    
    

if __name__ == '__main__':
    unittest.main()