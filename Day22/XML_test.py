#__author: ZhengNengjin
#__date: 2018/10/4

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test")
root = tree.getroot()

# 修改
for node in root.iter('year'):
	new_year = int(node.text) + 1
	node.text = str(new_year)
	node.set("updated", "yes")

tree.write("xmltest.xml")
