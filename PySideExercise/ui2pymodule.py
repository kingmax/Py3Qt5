#coding:utf-8
#ui2pymodule.py

import os, sys
from pysideuic import compileUi

cwd = os.getcwd()
uiFiles = [f for f in os.listdir(cwd) if f.endswith('.ui')]
print(uiFiles)

uifile = raw_input('input the ui filename:\n')
if uifile in uiFiles:
    name = os.path.splitext(uifile)[0]
    pyfile = open('%s.py'%name, 'w')
    compileUi(uifile, pyfile)
    pyfile.close()
    print('ok')
else:
    print('not found uifile:%s'%uifile)
    

