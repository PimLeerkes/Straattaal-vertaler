import requests
from pprint import pprint
import json

# Gaat uiteindelijk een loop worden, maar doet een request van de data en slaat het op
sources = 'http://straattaal.codefront.nl/?callback=&s='
response = requests.get(sources)
data = response.json()

# opschonen van de woorden
processed_data = []
for item in data:
    processed_item = {}
    processed_item[item["woord"].lower()] = item["betekenis"].lower()
    processed_data.append(processed_item)

with open("woorden.json",'w') as write_file:
    json.dump(processed_data, write_file, indent=4)

# pprint(response.json())
