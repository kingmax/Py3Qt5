#!/usr/bin/env python
#coding:utf-8
# Author:  LiYaJun --<kingmax.res@gmail.com>
# Purpose: Asset Tracking for Maya
# Created: 2013/9/11

import sys,os,shutil
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PySide.QtCore import *
from PySide.QtGui import *

#import maya.cmds as mc

#import sip
#import maya.OpenMayaUI as mui

##----------------------------------------------------------------------
def GetMayaWindow():
    #"""Get the maya main window as a QMainWindow instance"""
    ptr = mui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QObject)



########################################################################
class AssetTracking(QMainWindow):
    """AssetTracking for maya"""

    #----------------------------------------------------------------------
    def __init__(self, parent=None):
        """Constructor"""
        
        super(AssetTracking, self).__init__(parent)
        
        self._files = [] #fileNodes mc.ls(type='file')
        
        self.InitUI()
        
        
    """"""""""""
    #Properties:
    """"""""""""
    #----------------------------------------------------------------------
    def _getFiles(self):
        """"""
        return self._files
    #----------------------------------------------------------------------
    def _setFiles(self,v):
        if isinstance(v, list):
            self._files = v
    Files = property(_getFiles, _setFiles)
    
        
    #----------------------------------------------------------------------
    def InitUI(self):
        """init ui"""
        self.resize(1050, 650)
        self.setWindowTitle("Asset Tracking for Maya:: Dev By LiYaJun")
     
        self.CreateMenu()
        self.CreateMainToolBar()
        self.CollectFileData()
        self.CreateTable()
        self.CreateContextMenu()
        self.statusBar()
        
    #----------------------------------------------------------------------
    def CreateMenu(self):
        """init QAction & build main menu"""
        mainMenu = self.menuBar()
        
        #
        #File
        editMenu = mainMenu.addMenu("&File")
        self.setPath = QAction("Set Path...", self)
        self.setPath.setStatusTip("Specify asset path")
        self.setPath.triggered.connect(self.SetPath)
        editMenu.addAction(self.setPath)
        
        self.browse = QAction("Browse...", self)
        self.browse.setStatusTip("Browse image file")
        self.browse.triggered.connect(self.Browse)
        editMenu.addAction(self.browse)
        
        self.rename = QAction("Rename...", self)
        self.rename.setStatusTip("Rename image file and Update shader connection")
        self.rename.triggered.connect(self.Rename)
        editMenu.addAction(self.rename)
        editMenu.addSeparator()
        #---------------------------
        
        self.copyTo = QAction("Copy To...", self)
        self.copyTo.setStatusTip("Copy selected image to...")
        self.copyTo.triggered.connect(self.CopyTo)
        editMenu.addAction(self.copyTo)
        
        self.moveTo = QAction("Move To...", self)
        self.moveTo.setStatusTip("Move selected image to...")
        self.moveTo.triggered.connect(self.MoveTo)
        editMenu.addAction(self.moveTo)
        editMenu.addSeparator()
        #-----------------------------
        
        self.view = QAction("View Image", self)
        self.view.setStatusTip("View selected image")
        self.view.triggered.connect(self.View)
        editMenu.addAction(self.view)
        
        self.reveal = QAction("Reveal in explorer", self)
        self.reveal.setStatusTip("Reveal image file in explorer")
        self.reveal.triggered.connect(self.Reveal)
        editMenu.addAction(self.reveal)
        editMenu.addSeparator()
        #-----------------------------
        
        self.refresh = QAction("Refresh", self)
        self.refresh.setStatusTip("Refresh")
        self.refresh.triggered.connect(self.Refresh)
        editMenu.addAction(self.refresh)
        
        #
        #Sort
        sortMenu = mainMenu.addMenu("So&rt")
        
        self.sortA2Z = QAction("A->Z", self)
        self.sortA2Z.setStatusTip("Sort by A to Z")
        self.sortA2Z.triggered.connect(self.SortA2Z)
        sortMenu.addAction(self.sortA2Z)
        
        self.sortZ2A = QAction("Z->A", self)
        self.sortZ2A.setStatusTip("Sort by Z to A")
        self.sortZ2A.triggered.connect(self.SortZ2A)
        sortMenu.addAction(self.sortZ2A)
                
        self.sortByExtension = QAction("By Type", self)
        self.sortByExtension.setStatusTip("Sort by Type(file extension)")
        self.sortByExtension.triggered.connect(self.SortByExtension)
        sortMenu.addAction(self.sortByExtension)
        
        self.sortByStatus = QAction("By Status", self)
        self.sortByStatus.setStatusTip("Sort by file status")
        self.sortByStatus.triggered.connect(self.SortByStatus)
        sortMenu.addAction(self.sortByStatus)

        #
        #Select
        selByMenu = mainMenu.addMenu("&Select")
        
        self.highLightByObj = QAction("HighLight By Object", self)
        self.highLightByObj.setStatusTip("HighLight image file by selected object(geometry)")
        self.highLightByObj.triggered.connect(self.HighLightByObj)
        selByMenu.addAction(self.highLightByObj)
        
        self.highLightByMat = QAction("HighLight By Material", self)
        self.highLightByMat.setStatusTip("HighLight image file by selected material")
        self.highLightByMat.triggered.connect(self.HighLightByMat)
        selByMenu.addAction(self.highLightByMat)
        
        self.highLightByTex = QAction("HighLight By Texture", self)
        self.highLightByTex.setStatusTip("HighLight image file by selected texture(file node)")
        self.highLightByTex.triggered.connect(self.HighLightByTex)
        selByMenu.addAction(self.highLightByTex)
        selByMenu.addSeparator()
        #-------------------------------------
        
        self.highLightByKeyWord = QAction("HighLight By Keyword...", self)
        self.highLightByKeyWord.setStatusTip("HighLight image file by Keyword...(User Input)")
        self.highLightByKeyWord.triggered.connect(self.HighLightByKeyWord)
        selByMenu.addAction(self.highLightByKeyWord)
        selByMenu.addSeparator()
        #-------------------------------------
        
        self.selectGeometry = QAction("Select Geometry", self)
        self.selectGeometry.setStatusTip("Select relevant geometry")
        self.selectGeometry.triggered.connect(self.SelectGeometry)
        selByMenu.addAction(self.selectGeometry)
        
        self.selectMaterial = QAction("Select Material",self)
        self.selectMaterial.setStatusTip("Select relevant material(s)")
        self.selectMaterial.triggered.connect(self.SelectMaterial)
        selByMenu.addAction(self.selectMaterial)
        
    #----------------------------------------------------------------------
    def CreateContextMenu(self):
        """build context menu"""
        def AddSeparator():
            sp = QAction(self)
            sp.setSeparator(True)
            self.tb.addAction(sp)            
        
        self.tb.addAction(self.setPath)
        self.tb.addAction(self.browse)
        self.tb.addAction(self.rename)
        AddSeparator()
        self.tb.addAction(self.copyTo)
        self.tb.addAction(self.moveTo)
        AddSeparator()
        self.tb.addAction(self.view)
        self.tb.addAction(self.reveal)
        
        AddSeparator()
        self.tb.addAction(self.sortA2Z)
        self.tb.addAction(self.sortZ2A)
        self.tb.addAction(self.sortByExtension)
        self.tb.addAction(self.sortByStatus)
        
        AddSeparator()
        self.tb.addAction(self.highLightByObj)
        self.tb.addAction(self.highLightByMat)
        self.tb.addAction(self.highLightByTex)
        AddSeparator()
        self.tb.addAction(self.highLightByKeyWord)
        AddSeparator()
        self.tb.addAction(self.selectGeometry)
        self.tb.addAction(self.selectMaterial)        
        
        AddSeparator()
        self.tb.addAction(self.refresh)
        
        self.tb.setContextMenuPolicy(Qt.ActionsContextMenu)        
        
    
    #----------------------------------------------------------------------
    def CreateMainToolBar(self):
        """build toolBar"""
        toolBar = self.addToolBar("main")
        
        toolBar.addAction(self.refresh)
        toolBar.addSeparator()
        toolBar.addAction(self.setPath)
        toolBar.addAction(self.browse)
        toolBar.addAction(self.rename)
        toolBar.addSeparator()
        toolBar.addAction(self.copyTo)
        toolBar.addAction(self.moveTo)
        toolBar.addSeparator()
        toolBar.addAction(self.view)
        toolBar.addAction(self.reveal)
        
        #sortToolBar = self.addToolBar("sort")
        toolBar.addSeparator()
        toolBar.addSeparator()
        toolBar.addAction(self.sortA2Z)
        toolBar.addAction(self.sortZ2A)
        toolBar.addAction(self.sortByExtension)
        toolBar.addAction(self.sortByStatus)
        toolBar.addSeparator()
        toolBar.addAction(self.highLightByKeyWord)
        
        selToolBar = self.addToolBar("select")
        selToolBar.addAction(self.highLightByObj)
        selToolBar.addAction(self.highLightByMat)
        selToolBar.addAction(self.highLightByTex)
        selToolBar.addSeparator()
        selToolBar.addAction(self.selectGeometry)
        selToolBar.addAction(self.selectMaterial)
        
        
    #----------------------------------------------------------------------
    def CollectFileData(self):
        """Get all fileTextureName"""
        self.Files = ['c:/avatar.jpg', 'c:/sampledNormals.jpg']
        #self.Files = mc.ls(type='file')
        #self.FileNames = [mc.getAttr('%s.fileTextureName'%f) for f in self.Files]
        #self.FileDict = dict(zip(self.Files, self.FileNames))
        
    #----------------------------------------------------------------------
    def CreateTable(self):
        """build table"""
        
        header = ["Name", "Full Path", "Status", "Type", "File Node", ""]
        
        self.tb = QTableWidget(1000,len(header))
        self.tb.setHorizontalHeaderLabels(header)
        #self.tb.verticalHeader().setVisible(False)
        self.tb.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tb.setSelectionBehavior(QTableWidget.SelectRows)
        
        self.tb.setColumnWidth(0, 200) #Name
        self.tb.setColumnWidth(1, 700) #Full Path
        self.tb.setColumnWidth(2, 50)  #Status
        self.tb.setColumnWidth(3, 50)  #Type::Extension Name
        self.tb.setColumnWidth(len(header)-1, 1000) #theLast
        
        self.setCentralWidget(self.tb)
        #print(self.tb.rowHeight(0))
        #print(self.tb.columnWidth(0))
        
        for i in range(self.tb.rowCount()):
            self.tb.setRowHeight(i, 20)
        
        if self.Files:
            print(self.Files)
            myTable = MyTable.CreateFromFileNames(self.Files)
            print(myTable)
            for t in myTable:
                print(t)
        
        if self.Files:
            for r in range(len(self.Files)):
                fPath, fName = os.path.split(self.Files[r])
                fType = os.path.splitext(self.Files[r])[-1]
                for c in range(self.tb.columnCount()-1):
                    if c == 0:   #Name
                        self.tb.setItem(r, c, QTableWidgetItem(fName))
                    elif c == 1: #Full Path
                        self.tb.setItem(r, c, QTableWidgetItem(fPath))
                    elif c == 2: #Status
                        _status = QTableWidgetItem("OK" if os.path.exists(self.Files[r]) else "Missing")
                        _status.setTextAlignment(0x0044)
                        self.tb.setItem(r, c, _status)
                    elif c == 3: #Type
                        _type = QTableWidgetItem(fType)
                        _type.setTextAlignment(0x0044)
                        self.tb.setItem(r, c, _type)                    
            
        #self.Data = {"fileA.tga":["c:/fileA/", True, ".tga"]}
        #if self.Data:
            #keys = self.Data.keys()
            #values = self.Data.values()
            ##print(values)
            #for r in range(len(self.Data)):
                #for c in range((self.tb.columnCount()-1)):
                    ##self.tb.setItem(r, c, QTableWidgetItem(("%s,%s"%(data.keys()[r],c))))
                    #if c == 0:   #Name
                        #self.tb.setItem(r, c, QTableWidgetItem(keys[r]))
                    #elif c == 1: #Full Path
                        #self.tb.setItem(r, c, QTableWidgetItem(values[r][0]))
                    #elif c == 2: #Status
                        #item = QTableWidgetItem("OK" if values[r][1] else "Missing")
                        #item.setTextAlignment(0x0044)
                        #self.tb.setItem(r, c, item)
                    #elif c == 3: #Type
                        #item = QTableWidgetItem(os.path.splitext(keys[r])[-1])
                        #item.setTextAlignment(0x0044)
                        #self.tb.setItem(r, c, item)
        
    #----------------------------------------------------------------------        
    def resizeEvent(self, e):
        pass
        """
        changed = e.size() - e.oldSize()
        fullPathColWidth = self.tb.columnWidth(1)
        print(changed.width(), fullPathColWidth)
        if changed.width() > 0 and self.width() > 1000 and fullPathColWidth < self.width():
            self.tb.setColumnWidth(1, (fullPathColWidth + changed.width()))
        elif self.width() < 1000:
            self.tb.setColumnWidth(1, 700)
        """


    """"""""""""
    #Methods:
    """"""""""""
    #----------------------------------------------------------------------
    def SetPath(self):
        """set fileNode path"""
        print('setPath')
        
        if self.tb.selectedItems():
            rows = []
            for i in self.tb.selectionModel().selectedRows():
                rows.append(i.row())
            fd = unicode(QFileDialog.getExistingDirectory())
            print(fd)
            if fd and rows:
                for r in rows:
                    self.tb.item(r,1).setText(fd)
                    newPath = os.path.join(fd, unicode(self.tb.item(r,0).text()))
                    _status = "OK" if os.path.exists(newPath) else "Missing"
                    self.tb.item(r,2).setText(_status)
                    #update maya connections
        
    #----------------------------------------------------------------------
    def Browse(self):
        """browse image file"""
        print('browse image file')
        
        #self.tb.selectRow(5)
        rows = []
        for i in self.tb.selectionModel().selectedRows():
            rows.append(i.row())
        print(rows)
        
    #----------------------------------------------------------------------
    def Rename(self):
        """rename image file"""
        print('rename image file')
        
    #----------------------------------------------------------------------
    def CopyTo(self):
        """copy image file to..."""
        print('copy image file to...')
        
    #----------------------------------------------------------------------
    def MoveTo(self):
        """move image file to..."""
        print('move image file to...')
        
    #----------------------------------------------------------------------
    def View(self):
        """view image"""
        print('view image')
        
    #----------------------------------------------------------------------
    def Reveal(self):
        """reveal image in explorer"""
        print('reveal image in explorer')

    #----------------------------------------------------------------------
    def Refresh(self):
        """refresh file node information"""
        print('refresh')

    #
    #----------------------------------------------------------------------
    def SortA2Z(self):
        """sort by A to Z"""
        print('sort by A to Z')
        
    #----------------------------------------------------------------------
    def SortZ2A(self):
        """sort by Z to A"""
        print('sort by Z to A')

    #----------------------------------------------------------------------
    def SortByExtension(self):
        """sort by file extension"""
        print('sort by file extension')
        
    #----------------------------------------------------------------------
    def SortByStatus(self):
        """sort by file status"""
        print('sort by file status')

    #
    #----------------------------------------------------------------------
    def HighLightByObj(self):
        """highLight image file by selected obj(geometry)"""
        print('highLight image file by selected obj(geometry)')

    #----------------------------------------------------------------------
    def HighLightByMat(self):
        """highLight image file by selected material"""
        print('highLight image file by selected material')
        
    #----------------------------------------------------------------------
    def HighLightByTex(self):
        """highLight image file by selected texture(fileNode)"""
        print('highLight image file by selected texture(fileNode)')
        
    #----------------------------------------------------------------------
    def HighLightByKeyWord(self):
        """highLight image file by keyword (user input)"""
        print('highLight image file by keyword (user input)')
        
    #
    #----------------------------------------------------------------------
    def SelectGeometry(self):
        """select relevant geometry"""
        print('select relevant geometry')

    #----------------------------------------------------------------------
    def SelectMaterial(self):
        """select relevant material(s)"""
        print('select relevant material(s)')
        


########################################################################
class Row(object):
    """the row data"""

    #----------------------------------------------------------------------
    def __init__(self, fileName=None):
        """Constructor:: Row('c:/textures/bitmap.tga')"""
        
        fPath, fName = os.path.split(fileName)
        
        self._name = fName
        self._fullPath = fPath
        self._status = "OK" if os.path.exists(fileName) else "Missing"
        self._type = os.path.splitext(fileName)[-1]
        
    #----------------------------------------------------------------------
    def _getName(self):
        """"""
        return self._name
    #----------------------------------------------------------------------
    def _setName(self, v):
        """"""
        if isinstance(v, str) or isinstance(v, unicode) or isinstance(v, QString):
            self._name = v
            
    Name = property(_getName, _setName)
    
    #----------------------------------------------------------------------
    def _getFullPath(self):
        """"""
        return self._fullPath
    #----------------------------------------------------------------------
    def _setFullPath(self, v):
        """"""
        if os.path.isdir(v):
            self._fullPath = v
    
    FullPath = property(_getFullPath, _setFullPath)
    
    #----------------------------------------------------------------------
    def _getStatus(self):
        """"""
        return self._status
    
    Status = property(_getStatus)
    
    #----------------------------------------------------------------------
    def _getType(self):
        """"""
        return self._type
    
    Type = property(_getType)
    
    #----------------------------------------------------------------------
    def __str__(self):
        """"""
        return u"name:%s path:%s status:%s type:%s"%(self.Name, self.FullPath, self.Status, self.Type)
        


########################################################################
class MyTable(object):
    """
    MyRow Collection:: [ [key1, Row1], [key2, Row2] ... ]
    Similar to collections.OrderedDict, but it in Python2.7
    
    """
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._table = []
        self._start = 0

    #----------------------------------------------------------------------
    @staticmethod
    def CreateFromFileNames(fileNames=[]):
        """Factory Method:: Create a sorted table"""
        tb = MyTable()
        
        fileNames.sort()
        for f in fileNames:
            tb.Add(f, Row(f))
            #if os.path.isfile(f):
                #tb.Add(f, Row(f))
        
        return tb
        
    #----------------------------------------------------------------------
    def _getTable(self):
        """"""
        return self._table
    
    #----------------------------------------------------------------------
    def _setTable(self, v):
        """"""
        if isinstance(v, list):
            self._table = v
            
    Table = property(_getTable, _setTable)
    
    #----------------------------------------------------------------------
    def _getKeys(self):
        """fileName collection"""
        keys = []
        for item in self.Table:
            keys.append(item[0])
        return keys
    
    Keys = property(_getKeys)
    
    #----------------------------------------------------------------------
    def _getValues(self):
        """MyRow collection"""
        values = []
        for item in self.Table:
            values.append(item[1])
        return values
    
    Values = property(_getValues)
    
    #----------------------------------------------------------------------
    def _getCount(self):
        """"""
        return len(self.Table)
    
    Count = property(_getCount)
    
    #----------------------------------------------------------------------
    def __len__(self):
        """"""
        return self.Count
        
    #----------------------------------------------------------------------
    def Add(self, k, v):
        """append [k, v] in the Table collection, k is the UniqueFileName(ex: 'c:/textures/bitmap.tga'), v is a MyRow object"""
        if isinstance(v, Row):
            self.Table.append([k, v])
        else:
            raise TypeError("argument v type mustbe Row")
        
    #----------------------------------------------------------------------
    def Clear(self):
        """"""
        self.Table = []
        self.Keys = []
        self.Values = []
    
    #----------------------------------------------------------------------
    def Remove(self, k):
        """[].pop"""
        if self.Keys.count(k):
            index = self.Keys.index(k)
            self.Table.pop(index)
    
    #----------------------------------------------------------------------
    def __getitem__(self, k):
        """"""
        if isinstance(k, int):
            #raise KeyError("%s"%k)
            return self[self.Keys[k]]
        if isinstance(k, str) or isinstance(k, unicode) or isinstance(k, QString) and self.Keys.count(k):
            return self.Table[self.Keys.index(k)][-1]
    #----------------------------------------------------------------------
    def __setitem__(self, k, v):
        """"""
        if isinstance(k, str) or isinstance(k, unicode) or isinstance(k, QString) and isinstance(v, Row):
            if self.Keys.count(k):
                index = self.Keys.index(k)
                self.Table[index][-1] = v
            else:
                self.Add(k, v)
    
    #----------------------------------------------------------------------
    def SortByName(self, reverse=False):
        """sort by name(A-Z), reverse=True:(Z-A)"""
        if self.Count > 0:
            self.Table.sort(key=lambda item:item[-1].Name, reverse=reverse)
    
    #----------------------------------------------------------------------
    def SortByType(self, reverse=False):
        """"""
        if self.Count > 0:
            self.Table.sort(key=lambda item:item[-1].Type, reverse=reverse)
            
    #----------------------------------------------------------------------
    def SortByStatus(self, reverse=False):
        """"""
        if self.Count > 0:
            self.Table.sort(key=lambda item:item[-1].Status, reverse=reverse)
    
    #----------------------------------------------------------------------
    def __str__(self):
        """"""
        return unicode(["\n['%s': %s]\n"%(k,self[k]) for k in self.Keys])
    
    #----------------------------------------------------------------------
    def __iter__(self):
        """"""
        return self
    
    #----------------------------------------------------------------------
    def next(self):
        """"""
        if self._start >= self.Count:
            raise StopIteration
        index = self._start
        self._start += 1
        return self.Table[index]
    
    #----------------------------------------------------------------------
    def Reset(self):
        """"""
        self._start = 0
    
    
    
#----------------------------------------------------------------------
def Main():
    """test"""
    app = QApplication(sys.argv)
    #win = AssetTracking(GetMayaWindow())
    
    win = AssetTracking()
    win.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    Main()

