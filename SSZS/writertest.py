from writer import XMLWriter

root = XMLWriter()
result = root.generateXML('Lord Rot', '2', '250', 'mutiny', 'user written story goes in here')

print root.prettifyXML(result)
root.xMLToFile(result, 'test1.xml')


