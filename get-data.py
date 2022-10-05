import requests
from pprint import pprint
import json

# Gaat uiteindelijk een loop worden, maar doet een request van de data en slaat het op
sources = 'http://straattaal.codefront.nl/?callback=&s='
response = requests.get(source)

with open("test.json",'w') as write_file:
    json.dump(response.json(), write_file, indent=4)

# pprint(response.json())
