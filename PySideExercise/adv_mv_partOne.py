#coding:utf-8

from PySide.QtCore import *
from PySide.QtGui import *
import sys

class SimpleListModel(QAbstractListModel):
    def __init__(self, mlist):
        super(SimpleListModel, self).__init__()
        
        self._items = mlist
        
    def rowCount(self, parent=QModelIndex()):
        return len(self._items)
    
    
    def data(self, index, role=Qt.DisplayRole):
        '''elif role == Qt.BackgroundRole:
                    if index.row() % 2 == 0:
                        return QColor(Qt.gray)
                    else:
                        return QColor(Qt.lightGray)'''        
        if role == Qt.DisplayRole:
            return self._items[index.row()]
        elif role == Qt.EditRole:
            return self._items[index.row()]        
        else:
            return None
    
    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self._items[index.row()] = value
            QObject.emit(self, SIGNAL("dataChanged(const QModelIndex&, const QModelIndex &)"), index, index)
            return True
        return False
    
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
    
    def removeRows(self, row, count, parent=QModelIndex()):
        if row < 0 or row > len(self._items):
            return
        self.beginRemoveRows(parent, row, row+count-1)
        while count != 0:
            del self._items[row]
            count -= 1
        self.endRemoveRows()
        
    def addItem(self, item):
        self.beginInsertRows(QModelIndex(), len(self._items), len(self._items))
        self._items.append(item)
        self.endInsertRows()
        
class SimpleListView(QListView):
    def __init__(self, parent=None):
        super(SimpleListView, self).__init__(parent)
        self.setAlternatingRowColors(True)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        a = QAction("Delete Selected", self)
        QObject.connect(a, SIGNAL('triggered()', self, SLOT('onTriggered()')))
        self.addAction(a)
        
    @Slot()
    def onTriggered(self):
        self.model().removeRows(self.currentIndex().row(), 1)
        
class MyMainWindow(QWidget):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout()
        
        modelData = SimpleListModel(['test', 'test1t', 't3est', 't5est', 't3est'])
        view = SimpleListView()
        view.setModel(modelData)
        vbox.addWidget(view)
        
        view2 = SimpleListView()
        view2.setModel(modelData)
        vbox.addWidget(view2)
        
        hbox = QHBoxLayout()
        self._itemedit = QLineEdit()
        b = QPushButton('Add Item')
        QObject.connect(b, SIGNAL('clicked()'), self, SLOT('doAddItem()'))
        hbox.addWidget(self._itemedit)
        hbox.addWidget(b)
        
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
    @Slot()
    def doAddItem(self):
        self._model.addItem(self._itemedit.text())
        self._itemedit.setText('')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    sys.exit(app.exec_())
    