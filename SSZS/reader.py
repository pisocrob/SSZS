import xml.etree.ElementTree as ET

class XMLReader:
    def readXMLSource(self, path):
        tree = ET.parse(path)
        root = tree.getroot()

    def getAllXMLElements(self, root):
        voyage = root.findAll('voyage')
        name = voyage.find('name')
        years = voyage.find('yearsAtZee')
        echoes = voyage.find('Echeos')