from PySide import QtGui, QtCore
import sys

app = QtGui.QApplication([])

'''
item = QtGui.QStandardItem('item 1')
model = QtGui.QStandardItemModel()
model.setItem(0, 0, item)
tvSingle = QtGui.QTreeView()
tvSingle.setModel(model)
tvSingle.show()
'''

model = QtGui.QStandardItemModel(4, 4)
for row in range(4):
    for col in range(4):
        item = QtGui.QStandardItem('col {0} in row {1}'.format(col, row))
        model.setItem(row, col, item)

tableView = QtGui.QTableView()
tableView.setModel(model)
tableView.setMinimumWidth(450)
tableView.show()

treeView = QtGui.QTreeView()
treeView.setModel(model)
#treeView.show()


sys.exit(app.exec_())


'''
from PySide import QtGui, QtCore

# lets create a standard item, standard model and a treeview
item = QtGui.QStandardItem('item 1')

model = QtGui.QStandardItemModel()
model.setItem(0, 0, item);

treeViewSingle = QtGui.QTreeView()
treeViewSingle.setModel(model)
treeViewSingle.show()


# lets create a 4 by 4 data table to be shared by a tree and a tableview
model = QtGui.QStandardItemModel(4, 4)
#row, col = model.rowCount(), model.columnCount()
for row in range(4):
    for col in range(4):
        item = QtGui.QStandardItem('col {0} in row {1}'.format(col, row))
        model.setItem(row, col, item);

tableView = QtGui.QTableView()
tableView.setModel(model)
tableView.show()

treeView = QtGui.QTreeView()
treeView.setModel(model)
treeView.show()
'''