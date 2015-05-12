from writer import XMLWriter
from xml.etree.ElementTree import tostring

root = XMLWriter()
result = root.generateXML('Catpain pugWeshington', '4', '250')

print root.XMLToString(result)

root.XMLToFile(result, 'test1.txt')