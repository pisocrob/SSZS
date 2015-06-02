import xml.etree.ElementTree as ET

class XMLReader(object):
    nameList = ['name', 'years', 'echoes', 'coD', 'zeeStory']

    def __init__(self):
        self.tree = None
        self.root = None
        self.voyage = None
        self.name = None
        self.years = None
        self.echoes = None
        self.coD = None
        self.zeeStory = None
        self.valueList = []
        self.voyageDict = {}


    def readXMLSource(self, path):
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()

        for child in self.root:
            self.valueList.append(child.text)

        self.voyageDict = dict(zip(XMLReader.nameList,self.valueList))

            