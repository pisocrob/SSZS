import json

jsonFile = open('Autosave.json')
jsonParsed = jsonFile.read()
jsonFile.close()
backupFile = open('AutosaveBackup.json', 'w')
backupFile.write(jsonParsed)
backupFile.close()
parsedJson = json.loads(jsonParsed)

userJson = parsedJson['QualitiesPossessedList'][0]['AssociatedQualityId']

for x in parsedJson['QualitiesPossessedList']:
    if x['AssociatedQualityId']==102028:
        print x
