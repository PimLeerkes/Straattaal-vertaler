import requests
from pprint import pprint
import json

# Gaat uiteindelijk een loop worden, maar doet een request van de data en slaat het op
sources = 'http://straattaal.codefront.nl/?callback=&s='
response = requests.get(sources)


# opslaan van woorden
with open("woorden.json",'w') as write_file:
    json.dump(response.json(), write_file, indent=4)

# opschonen van de opgeslagen woorden

lowercase_woorden = []
with open("woorden.json", "r") as data:
    woorden = json.load(data)
    for woord in woorden:
        lowercase_woord = {}
        for key, value in woord.items():
            lowercase_woord[key] = value.lower()
        lowercase_woorden.append(lowercase_woord)

with open("woorden.json",'w') as write_file:
    json.dump(lowercase_woorden, write_file, indent=4)

# pprint(response.json())
