from xml.etree.ElementTree import Element, SubElement, tostring
#from ElementTree_pretty import prettify
class XMLWriter:

	def generateXML(self, vname, vyears, vechoes):
		root = Element('voyage')
		name = SubElement(root, 'name')
		name.text = vname

		years = SubElement(root, 'YearsAtZee')
		years.text = vyears

		echoes = SubElement(root, 'Echoes')
		echoes.text = vechoes

		return root

	def XMLToString(self, root):
		return tostring (root)

	def XMLToFile(self, XMLObject, filename):
		outFile = open(filename, 'w')
		outFile.write(tostring(XMLObject))