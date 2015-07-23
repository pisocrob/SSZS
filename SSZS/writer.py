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
        #maybe get rid of outfile var?
        self.outFile = None
        self.roughString = None
        self.prettyString = None

        #Maybe change to take list as parameter?
    def generateXML(self, name, years, echoes, coD, zeeStory):
        self.root = Element('Voyage')
        self.name = SubElement(self.root, 'Name')
        self.name.text = name

        self.years = SubElement(self.root, 'YearsAtZee')
        self.years.text = years

        self.echoes = SubElement(self.root, 'Echoes')
        self.echoes.text = echoes

        #coD is short for Cause of Death
        self.coD = SubElement(self.root, 'CauseOfDeath')
        self.coD.text = coD

        self.zeeStory = SubElement(self.root, 'ZeeStory')
        self.zeeStory.text = zeeStory

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