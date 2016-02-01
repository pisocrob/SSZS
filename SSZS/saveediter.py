import json
import sys

jsonFile = open('Autosave.json')
jsonData = jsonFile.read()
parsedJson = json.loads(jsonData)
jsonFile.close()
backupFile = open('AutosaveBackup.json', 'w')
backupFile.write(jsonData)
backupFile.close()

if sys.argv[1]=='echoes':
    for x in parsedJson['QualitiesPossessedList']:
        if x['AssociatedQualityId']==102028:
            if sys.argv[2]!=None:
                x['Level']=sys.argv[2]
            else:
                x['level']=99999
            jsonFile = open('Autosave.json', 'w+')
            jsonFile.write(json.dumps(parsedJson))
            jsonFile.close()

elif sys.argv[1]=='fuel':
    for x in parsedJson['QualitiesPossessedList']:
        if x['AssociatedQualityId']==102027:
            if sys.argv[2]!=None:
                x['Level']=sys.argv[2]
            else:
                x['level']=10
            jsonFile = open('Autosave.json', 'w+')
            jsonFile.write(json.dumps(parsedJson))
            jsonFile.close()

elif sys.argv[1]=='supplies':
    for x in parsedJson['QualitiesPossessedList']:
        if x['AssociatedQualityId']==102026:
            if sys.argv[2]!=None:
                x['Level']=sys.argv[2]
            else:
                x['level']=10
            jsonFile = open('Autosave.json', 'w+')
            jsonFile.write(json.dumps(parsedJson))
            jsonFile.close()