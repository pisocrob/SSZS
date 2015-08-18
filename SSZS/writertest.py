from writer import XMLWriter

root = XMLWriter()
info = ['Lord Rot', '2', '250', 'Mutiny', "Storm's curse is a powerful thing"]
result = root.generateXML(info)

print root.prettifyXML(result)
root.xmlToFile(result)


