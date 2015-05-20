from writer import XMLWriter
from reader import XMLReader

root = XMLWriter()
result = root.generateXML('Catpain pugWeshington', '4', '250')

print root.prettifyXML(result)
root.xMLToFile(result, 'test1.xml')


reader = XMLReader()
reader.readXMLSource('test1.xml')
print reader.echoes