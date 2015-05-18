from writer import XMLWriter

root = XMLWriter()
result = root.generateXML('Catpain pugWeshington', '4', '250')

print root.XMLToString(result)

root.XMLToFile(result, 'test1.xml')