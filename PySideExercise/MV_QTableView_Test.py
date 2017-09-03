#coding:utf-8

import sys
from PySide.QtCore import *
from PySide.QtGui import *

sys.path.append(r'D:\CloudRenderFarm\Plugins\Houdini\SubmitPlugin\scripts\python\HPRender')
from hpHoudiniLib import *

taskList = []
a = Task()
a.Index = 1
a.Rop = 'mantral1'
a.Driver = '/out/mantra1'
a.RenderEngine = 'raytrace'
a.Take = '_current_'
a.Camera = '/obj/cam1'
a.OutputFileName = r'd:\render\test.mantra1.$F4.exr'
a.ExtraImages = []
a.Start = 0
a.End = 10
a.Step = 1
a.FrameListExp = '0-10x1'
a.FrameList = [0]
a.FrameCount = len(a.FrameList)
a.Width = 400
a.Height = 300
a.PixelAspect = 1.0
#determined by the user on the UI
a.PreviewRend = True
a.PreRendList = [0,5,10]
a.ContinueAfterPreRend = True
taskList.append(a)

class TaskModel(QAbstractTableModel):
    def __init__(self, taskList):
        super(TaskModel, self).__init__()
        self._headers = ['ROP', 'Camera', 'Take', 'Range', 'Resolution', 'Preview', 'Output']
        self._taskList = taskList
        
    def rowCount(self, parent=QModelIndex()):
        return len(self._taskList)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)
    
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._taskList[index.row()]
        elif role == Qt.BackgroundRole:
            if index.row() % 2 == 0:
                return QColor(Qt.gray)
            else:
                return QColor(Qt.lightGray)
        else:
            return None
        
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
    
        
    
class TaskTableModel(QAbstractTableModel):
    def __init__(self, taskList=[], parent=None):
        super(TaskTableModel, self).__init__(parent)
        self._headers = ['ROP', 'Camera', 'Range', 'Resolution', 'Preview', 'Output']
        self._taskList = taskList
        self._ropCheckState = {}
        self._previewCheckState = {}

    def rowCount(self, index=QModelIndex()):
        return len(self._taskList)

    def columnCount(self, index=QModelIndex()):
        return len(self._headers)
    
    def headerData(self, column, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[column]
        #return None

    def data(self, index, role=Qt.DisplayRole):
        col = index.column()
        if role == Qt.DisplayRole:
            task = self._taskList[index.row()]   
            #['ROP', 'Camera', 'Range', 'Resolution', 'Preview', 'Output']
            if col == 0:
                return task.Rop
            elif col == 1:
                return task.Camera
            elif col == 2:
                return task.FrameListExp
            elif col == 3:
                return '%s x %s'%(task.Width, task.Height)
            elif col == 4:
                return ','.join([str(n) for n in task.PreRendList])
            elif col == 5:
                return task.OutputFileName
            else:
                return None
        if role == Qt.CheckStateRole:
            if col == 0:
                if self._ropCheckState.has_key(col):
                    return self._ropCheckState[col]
                else:
                    return Qt.Unchecked
            elif col == 4:
                if self._previewCheckState.has_key(col):
                    return self._previewCheckState[col]
                else:
                    return Qt.Unchecked

        #return None


    def insertRows(self, position, rows=1, index=QModelIndex()):
        """ Insert a row into the model. """
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)

        for row in range(rows):
            self._taskList.insert(position + row, {"name":"", "address":""})

        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove a row from the model. """
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)

        del self._taskList[position:position+rows]

        self.endRemoveRows()
        return True

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        
        row = index.row()
        col = index.column()
        if role == Qt.CheckStateRole:
            if col == 0:
                self._ropCheckState[row] = Qt.Checked if value == Qt.Checked else Qt.Unchecked
                print(self._ropCheckState)
                return True
            elif col == 4:
                self._previewCheckState[row] = Qt.Checked if value == Qt.Checked else Qt.Unchecked
                print(self._previewCheckState)
                return True

        if role == Qt.EditRole and 0 <= row < len(self._taskList):
            task = self._taskList[row]
            #['ROP', 'Camera', 'Range', 'Resolution', 'Preview', 'Output']
            if col == 4:
                print(value)
            else:
                return False

            self.dataChanged.emit(index, index)
            return True

        return True

    def flags(self, index):
        _flags = QAbstractTableModel.flags(self, index)
        col = index.column()
        if col == 0:
            return _flags | Qt.ItemIsUserCheckable
        elif col == 4:
            return _flags | Qt.ItemIsUserCheckable | Qt.ItemIsEditable

        return _flags

class Win2(QMainWindow):
    def __init__(self):
        super(Win2, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(750, 411)
        model = TaskTableModel(taskList) #TaskTableModel([{'name':'jason', 'address':'cn'}, {'name':'kingmax', 'address':'us'}])
        print(model.index(0,0))
        view = QTableView(self)
        view.resize(700,200)
        view.setModel(model)
        


class Win(QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(550,300)
        self.setWindowTitle('QTableView')
        
        #self.model = QStandardItemModel(1,5)
        #headers = ['Name', 'NO.', 'Sex', 'Age', 'College']
        #self.model.setHorizontalHeaderLabels(headers)
        self.model = TaskModel(['a', 'b'])
        
        
        self.view = QTableView(self)
        self.view.setMinimumSize(500, 200)
        self.view.verticalHeader().hide() 
        self.view.setModel(self.model)
        #self.view.setEnabled(False)
        
        self.btn = QPushButton('Test', self)
        self.btn.move(100, 200)
        self.btn.clicked.connect(self.test)
        
    def test(self):
        print(self.model.flags(self.model.index(0)))
        '''
        sender = self.sender()
        item = QStandardItem(u'张三')
        #item.setFlags(Qt.ItemIsUserCheckable)
        item.setCheckable(True)
        self.model.setItem(0, 0, item)
        item = QStandardItem('1,3,5')
        item.setCheckable(True)
        self.model.setItem(0, 4, item)
        '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win2()
    win.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    