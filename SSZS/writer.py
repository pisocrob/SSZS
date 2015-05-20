from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom
#from ElementTree_pretty import prettify
class XMLWriter(object):

    def __init__(self):
        self.root = None
        self.name = None
        self.years = None
        self.echoes = None
        self.outFile = None
        self.roughString = None
        self.prettyString = None

    def generateXML(self, vname, vyears, vechoes):
        self.root = Element('voyage')
        self.name = SubElement(self.root, 'name')
        self.name.text = vname

        self.years = SubElement(self.root, 'YearsAtZee')
        self.years.text = vyears

        self.echoes = SubElement(self.root, 'Echoes')
        self.echoes.text = vechoes


    def xMLToString(self, XMLObject):
        return ElementTree.tostring(XMLObject, 'utf-8')

    def xMLToFile(self, XMLObject, filename):
        self.outFile = open(filename, 'w')
        self.outFile.write(ElementTree.tostring(XMLObject, 'utf-8', 'xml'))

        #recurrent 'no attribute error' - Google suggests indenting but
        #this seems to be in order?

    def prettifyXML(self, XMLObject):
        self.roughString = ElementTree.tostring(XMLObject, 'utf-8', 'xml')
        self.prettyString = minidom.parseString(self.roughString)
        return self.prettyString.toprettyxml (indent="    ")