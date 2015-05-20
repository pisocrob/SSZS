import xml.etree.ElementTree as ET

class XMLReader(object):

    def __init__(self):
        self.voyage = None
        self.name = None
        self.years = None
        self.echoes = None
        self.tree = None
        self.root = None


    def readXMLSource(self, path):
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        #self.voyage = self.root.findall('voyage')
        self.name = self.root.get('name')
        self.years = self.root.get('yearsAtZee')
        self.echoes = self.root.get('Echoes')