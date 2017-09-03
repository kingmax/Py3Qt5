#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee (kingmax_res@163.com | 184327932@qq.com)
  Purpose: 
  Created: 2017/8/13
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

########################################################################
class Tetrominoe(QObject):
    """"""
    NoShape = 0
    ZShape  = 1
    SShape  = 2
    LineShape=3
    TShape  = 4
    SquareShape=5
    LShape  = 6
    MirroredLShape=7
    

########################################################################
class Shape(QObject):
    """"""
    #all shape coord
    coordsTable = (
        ( (0, 0),   (0, 0),  (0, 0),   (0, 0)  ),  #Empty
        ( (0, -1),  (0, 0),  (-1, 0),  (-1, 1) ),  #S shape
        ( (0, -1),  (0, 0),  (1, 0),   (1, 1)  ),  #Z shape
        ( (0, -1),  (0 ,0),  (0, 1),   (0, 2)  ),  #Line shape
        ( (-1, 0),  (0, 0),  (1, 0),   (0, 1)  ),  #T shape
        ( (0, 0),   (1, 0),  (0, 1),   (1, 1)  ),  #Square shape
        ( (-1,-1),  (0, -1), (0, 0),   (0, 1)  ),  #Mirrored L shape
        ( (1, -1),  (0, -1), (0, 0),   (0, 1)  )   #L shape
    )
    
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape
        self.setShape(Tetrominoe.NoShape)
        
    #----------------------------------------------------------------------
    def shape(self):
        """"""
        return self.pieceShape
    
    #----------------------------------------------------------------------
    def setShape(self, shape):
        """"""
        tabel = Shape.coordsTable[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = tabel[i][j]
        self.pieceShape = shape
        
    #----------------------------------------------------------------------
    def setRandomShape(self):
        """"""
        self.setShape(random.randint(1, 7))
        
    #----------------------------------------------------------------------
    def x(self, index):
        """return x coordinate"""
        return self.coords[index][0]
    
    #----------------------------------------------------------------------
    def y(self, index):
        """return y coordinate"""
        return self.coords[index][1]
    
    #----------------------------------------------------------------------
    def setX(self, index, x):
        """"""
        self.coords[index][0] = x
        
    #----------------------------------------------------------------------
    def setY(self, index, y):
        """"""
        self.coords[index][1] = y
        
    #----------------------------------------------------------------------
    def minX(self):
        """"""
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])
            
        return m
    
    #----------------------------------------------------------------------
    def minY(self):
        """"""
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
            
        return m
    
    #----------------------------------------------------------------------
    def maxX(self):
        """"""
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])
            
        return m
    
    #----------------------------------------------------------------------
    def maxY(self):
        """"""
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])
            
        return m
    
    #----------------------------------------------------------------------
    def rotateLeft(self):
        """rotates shape to the left"""
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        
        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))
            
        return result
    
    #----------------------------------------------------------------------
    def rotateRight(self):
        """rotates shape to the right"""
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        
        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))
            
        return result
    
    
########################################################################
class Board(QFrame):
    """"""
    msg2Statusbar = pyqtSignal(str)
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300
    
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        super(Board, self).__init__(parent)
        self.initBoard()
        
    #----------------------------------------------------------------------
    def initBoard(self):
        """"""
        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False
        
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []
        
        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
        
    #----------------------------------------------------------------------
    def clearBoard(self):
        """clears shapes from the board"""
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)
            
    #----------------------------------------------------------------------
    def shapeAt(self, x, y):
        """determines shape at the position"""
        return self.board[(y * Board.BoardWidth) + x]
    
    #----------------------------------------------------------------------
    def setShapeAt(self, x, y, shape):
        """set a shape at the board"""
        self.board[(y * Board.BoardWidth) + x] = shape
        
    #----------------------------------------------------------------------
    def squareWidth(self):
        """returns the width of one square"""
        return self.contentsRect().width() // Board.BoardWidth
    
    #----------------------------------------------------------------------
    def squareHeight(self):
        """returns the height of one square"""
        return self.contentsRect.height() // Board.BoardHeight
    
    #----------------------------------------------------------------------
    def start(self):
        """starts game"""
        if self.isPaused:
            return
        
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()
        self.msg2Statusbar.emit(str(self.numLinesRemoved))
        self.newPiece()
        self.timer.start(Board.Speed, self)
        
    #----------------------------------------------------------------------
    def newPiece(self):
        """create a new shape"""
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
        
        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit('Game over')
            
    #----------------------------------------------------------------------
    def tryMove(self, newPiece, newX, newY):
        """tries to move a shape"""
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
            
            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False
            
        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        
        return True
    
    #----------------------------------------------------------------------
    def drawSquare(self, painter, x, y, shape):
        """draw a square of a shape"""
        colors = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                  0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        
        color = QColor(colors[shape])
        painter.fillRect(x+1, y+1, self.squareWidth()-2, self.squareHeight()-2, color)
        
        painter.setPen(color.lighter())
        painter.drawLine(x, y+self.squareHeight()-1, x, y)
        painter.drawLine(x, y, x+self.squareWidth()-1, y)
        
        painter.setPen(color.darker())
        painter.drawLine(x+1, y+self.squareHeight()-1, x+self.squareWidth()-1, y+self.squareHeight()-1)
        painter.drawLine(x+self.squareWidth()-1, y+self.squareHeight()-1, x+self.squareWidth()-1, y+1)
        
        


########################################################################
class Tetris(QMainWindow):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Tetris, self).__init__()
        self.initUI()

    #----------------------------------------------------------------------
    def initUI(self):
        """"""
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)
        
        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris game')
        self.show()
        
    #----------------------------------------------------------------------
    def center(self):
        """centers the window on the screen"""
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height()-size.height())/2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Tetris()
    sys.exit(app.exec_())