import houxmlrpc

hou = houxmlrpc.ServerProxy('http://localhost:50001').hou

hou.hipFile.clear()

geo = hou.node('/obj').createNode('geo')
geo.children()[0].destroy()
box = geo.createNode('box')
box.setDisplayFlag(True)
box.setRenderFlag(True)
box.setCurrent(True)
box.moveToGoodPosition()

hou.hipFile.save('c:/hou001_in_wingIDE.hip')