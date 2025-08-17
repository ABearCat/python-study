from pprint import pprint
import json
import random


with open('data.json', 'r', encoding='utf-8') as data:
    fileData = json.load(data)

filteredData = []
sortedByVersion = []
sortedById = []
noDuplicates = []
prevname = ""

for person in fileData:
    newBio = person.get("bio").replace(' ', '')
    updatedPerson = {"name": person.get("name"), "id": random.randint(1, 10000000000), "version": person.get("version"), "bio": newBio}
    pprint(updatedPerson)
    filteredData.append(updatedPerson)

sortedByVersion = sorted(filteredData, key=lambda x: x['version'])
sortedById = sorted(filteredData, key = lambda x: x['id'])

sortedByName = sorted(filteredData, key = lambda x: x['name'])
for person in sortedByName:
    if (prevname != person.get("name")):

        updatedPerson = {"name": person.get("name"), "id": person.get("id"), "version": person.get("version"), "bio": newBio}
        noDuplicates.append(updatedPerson)
        prevname = person.get("name")

#sorts by version number
with open('version.json', 'w', encoding='utf-8') as output:
    json.dump(sortedByVersion, output, indent = 4)

#applies a bad id system and sorts them by the new id
with open('id.json', 'w', encoding='utf-8') as output:
    json.dump(sortedById, output, indent = 4)

#sorts by name and only allows 1 user per name
with open('filtered.json', 'w', encoding='utf-8') as output:
    json.dump(noDuplicates, output, indent = 4)