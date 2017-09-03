#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: 2016/10/28
"""



class Test():
    def __init__(self):
        self._files = []
        
    @property
    def files(self):
        return self._files
    
    @files.setter
    def files(self, value):
        if isinstance(value, list):
            self._files = value
    
    def _getFiles(self):
        return self._files
    
    def _setFiles(self, value):
        if isinstance(value, list):
            self._files = value
            
    Files = property(_getFiles, _setFiles)
            
    def __str__(self):
        return """
        files:       %s
        """%(self._files)


if __name__ == '__main__':
    test = Test()
    print(test)
    test.Files = [1,2,3]
    print(test)
    test.files = [4,5]
    print(test)