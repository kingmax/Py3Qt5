#createBox.py
#coding:utf-8

import hou

obj = hou.node('/obj')
geo = obj.createNode('geo')
geo.children()[0].destroy()
font = geo.createNode('font')
font.setParms({'text':'from WingIDE'})
geo.setName('HiWingIDE')

box = obj.createNode('geo').createNode('box')
box.setDisplayFlag(True)
box.setRenderFlag(True)
box.setCurrent(True)
box.moveToGoodPosition()

pos = hou.node('/obj/geo1').parmTuple('t')
print(pos.eval())
pos.set((0, 0.5, 0))
print(pos.eval())

objNode = box.parent()
objNode.setName('newBox')
green = hou.Color((0,1,0))
objNode.setColor(green)
objNode.moveToGoodPosition()

hou.hipFile.save('c:/fromWingIDE.hip')

print('ok')