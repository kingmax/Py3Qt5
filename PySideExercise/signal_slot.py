#http://pythoncentral.io/pysidepyqt-tutorial-creating-your-own-signals-and-slots/

import sys
from PySide.QtCore import QObject, Signal, Slot

class Circle(QObject):
    resized = Signal(int)
    moved = Signal(int, int)
    
    def __init__(self, x, y, r):
        super(Circle, self).__init__()
        
        self._x = x
        self._y = y
        self._r = r
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        self._x = new_x
        self.moved.emit(new_x, self.y)
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, new_y):
        self._y = new_y
        self.moved.emit(self.x, new_y)
        
    @property
    def r(self):
        return self._r
    
    @r.setter
    def r(self, new_r):
        self._r = new_r
        self.resized.emit(new_r)
        
        
@Slot(int, int)
def on_moved(x, y):
    print('Circle was moved to (%s,%s).'%(x, y))
    
@Slot(int)
def on_resized(r):
    print('Circle was resized to radius %s.'%r)


if __name__ == '__main__':
    c = Circle(5, 5, 4)
    c.moved.connect(on_moved)
    c.resized.connect(on_resized)
    
    c.x += 1
    c.r += 1
    