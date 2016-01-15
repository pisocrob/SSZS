import json
import sys

jsonFile = open('Autosave.json')
jsonData = jsonFile.read()
parsedJson = json.loads(jsonData)
jsonFile.close()
backupFile = open('AutosaveBackup.json', 'w')
backupFile.write(jsonData)
backupFile.close()

class getValues(object):

    def __init__(self):
    self.objectType = None
    self.objectValue = None
    self.quantity = None

    def getBasics(self, objectType):
        if self.objectType=="fuel":
            self.objectValue=102027
        elif self.objectType=="echoes":
            self.objectValue=102028
        elif self.objectType=="supplies":
            self.objectValue=102026

        for x in parsedJson['QualitiesPossessedList']:
            if x['AssociatedQualityId']==self.objectValue:
                self.quantity=x['Level']
        return self.quantity

class setValues(object):
    def __init__(self):
    self.objectType = None
    self.objectValue = None
    self.quantity = None

    def setValues(self, objectType, quantity):
        if self.objectType=="fuel":
            self.objectValue=102027
        elif self.objectType=="echoes":
            self.objectValue=102028
        elif self.objectType=="supplies":
            self.objectValue=102026

        or x in parsedJson['QualitiesPossessedList']:
            if x['AssociatedQualityId']==self.objectValue:
                x['Level']=self.quantity
            jsonFile = open('Autosave.json', 'w+')
            jsonFile.write(json.dumps(parsedJson))
            jsonFile.close()