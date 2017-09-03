import houxmlrpc

hou = houxmlrpc.ServerProxy('http://localhost:50001').hou
geo = hou.node('/obj').createNode('geo')
geo.children()[0].destroy()
font = geo.createNode('font')
font.setParms({'text':'WingIDE is connected'})