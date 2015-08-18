from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom
import time
import datetime


#TODO: Add dateAdded attribute for each xml entry
class XMLWriter(object):

    def __init__(self):
        self.root = None
        self.tree = None
        self.storyList = None
        self.name = None
        self.years = None
        self.echoes = None
        self.coD = None
        self.zeeStory = None
        self.fileName = None
        self.roughString = None
        self.prettyString = None
        self.timeStamp = time.time()
        self.timeString = None

        #coD is Cause of Death
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

    def xmlToString(self, xmlObject):
        return tostring(xmlObject)

    """time stamp uses everything from year to second to ensure unique file name in the event that
    a Captain's name is reused."""
    #TODO: Add flag for removal of whitespace
    def xmlToFile(self, xmlObject):
        self.tree = ElementTree(xmlObject)
        self.timeString = datetime.datetime.fromtimestamp(self.timeStamp).strftime(' %y%m%d%H%M%S')
        self.name = xmlObject[0].text
        self.tree.write(self.name + self.timeString + '.xml', 'UTF-8', 'xml')

    def prettifyXML(self, xmlObject):
        self.roughString = tostring(xmlObject)
        self.prettyString = minidom.parseString(self.roughString)
        return self.prettyString.toprettyxml (indent="    ")