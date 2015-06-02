from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom

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
    def generateXML(self, name, years, echoes, coD, zeeStory):
        self.root = Element('Voyage')
        self.name = SubElement(self.root, 'Name')
        self.name.text = name

        self.years = SubElement(self.root, 'YearsAtZee')
        self.years.text = years

        self.echoes = SubElement(self.root, 'Echoes')
        self.echoes.text = echoes

        self.coD = SubElement(self.root, 'CauseOfDeath')
        self.coD.text = coD

        self.zeeStory = SubElement(self.root, 'ZeeStory')
        self.zeeStory.text = zeeStory

        return self.root


    def xMLToString(self, xMLObject):
        return tostring(xMLObject)

    def xMLToFile(self, xMLObject, filename):
        self.tree = ElementTree(xMLObject)
        self.tree.write(filename, 'UTF-8', 'xml')

    def prettifyXML(self, xMLObject):
        self.roughString = tostring(xMLObject)
        self.prettyString = minidom.parseString(self.roughString)
        return self.prettyString.toprettyxml (indent="    ")