# -*- coding: utf-8 -*-


from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)

from xml.etree.ElementTree import tostring
print(tostring(e))
