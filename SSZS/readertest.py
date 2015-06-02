from reader import XMLReader

reader = XMLReader()
reader.readXMLSource('test1.xml')
print reader.root.tag
# print reader.root.attrib
#print reader.valueList[0]

for keys, values in reader.voyageDict.items():
    print(keys)
    print(values)

