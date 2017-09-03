#!/usr/bin/env python
#coding:utf-8
#ET.py

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem





#root = ET.Element('html')

#head = ET.SubElement(root, 'head')

#title = ET.SubElement(head, 'title')
#title.text = u'Page Title: 页面  < you & her'

#body = ET.SubElement(root, 'body')
#body.set('bgcolor', '#aabbcc')
#body.text = 'Hello, World!'

#indent(root)
#tree = ET.ElementTree(root)

#rt = ET.parse('page.html').getroot()
#print(rt, type(rt))
#indent(rt)
#ET.dump(rt)

#tree.write('page.html', encoding='UTF-8', xml_declaration=True, method='xml')