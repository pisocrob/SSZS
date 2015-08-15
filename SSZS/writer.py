from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom


#TODO: Add dateAdded attribute for each xml entry
class XMLWriter(object):

    def __init__(self):
        self.root = None
        self.tree = None
        self.name = None
        self.years = None
        self.echoes = None
        self.coD = None
        self.zeeStory = None
        self.outFile = None
        self.roughString = None
        self.prettyString = None

        #coD is short for Cause of Death
    def generateXML(self, storyList):
        self.root = Element('Voyage')
        self.name = SubElement(self.root, 'Name')
        self.name.text = storyList[0]

        self.years = SubElement(self.root, 'YearsAtZee')
        self.years.text = storyList[1]

        self.echoes = SubElement(self.root, 'Echoes')
        self.echoes.text = storyList[2]

        self.coD = SubElement(self.root, 'CauseOfDeath')
        self.coD.text = storyList[3]

        self.zeeStory = SubElement(self.root, 'ZeeStory')
        self.zeeStory.text = storyList[4]

        return self.root


    def xMLToString(self, xmlObject):
        return tostring(xmlObject)

    def xMLToFile(self, xmlObject, filename):
        self.tree = ElementTree(xmlObject)
        self.tree.write(filename, 'UTF-8', 'xml')

    def prettifyXML(self, xmlObject):
        self.roughString = tostring(xmlObject)
        self.prettyString = minidom.parseString(self.roughString)
        return self.prettyString.toprettyxml (indent="    ")