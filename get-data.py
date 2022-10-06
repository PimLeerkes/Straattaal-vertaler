import requests
import json

# Gaat uiteindelijk een loop worden, maar doet een request van de data en slaat het op

def save_to_file(lijst):
    with open("woorden.json",'w') as write_file:
         json.dump(lijst, write_file, indent=4)

def json_api_to_list():
    source = 'http://straattaal.codefront.nl/?callback=&s='
    response = requests.get(source)
    # opschonen van de woorden
    processed_data = []
    for item in response.json():
        processed_item = {item["woord"].lower(): item["betekenis"].lower()}
        processed_data.append(processed_item)
    return processed_data

def meerwoorden():
    with open("meerwoorden.txt", "r") as data:
        processed_data = []
        for woord in data:
            woord = woord.split("=")
            woord[1] = woord[1].strip()
            woord[0] = woord[0].split(",")
            woord[1] = woord[1].split(",")
            for w in woord[1]:
                for v in woord[0]:
                    processed_data.append({w: v})
        return processed_data

def main():
    merged_list = meerwoorden() + json_api_to_list()
    save_to_file(merged_list)

if __name__ == '__main__':
    main()    
