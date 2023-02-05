import requests
import json
import re
import os
import sys

def save_to_file(lijst):
    with open("./app/data/woorden.json",'w') as write_file:
         json.dump(lijst, write_file, indent=4)

def json_api_to_list():
    source = 'http://straattaal.codefront.nl/?callback=&s='
    response = requests.get(source)
    # formateren van de woorden
    processed_data = []
    for item in response.json():
        processed_item = {item["betekenis"].lower().strip(): item["woord"].lower().strip()}
        processed_data.append(processed_item)
    return processed_data

def meerwoorden():
    with open("./app/data/meerwoorden.txt", "r") as data:
        processed_data = []
        for woord in data:
            woord = woord.split("=")
            woord[1] = woord[1].strip()
            woord[0] = woord[0].split(",")
            woord[1] = woord[1].split(",")
            for w in woord[0]:
                for v in woord[1]:
                    processed_data.append({w.lower(): v.lower()})
        return processed_data

# lists the values with the same key
def list_values(ls):
    result = dict()
    for d in ls:
        for k, v in d.items():
            k = re.sub("[^A-Za-z0-9\s]", '', k)
            current = result.get(k, [])
            current.append(re.sub("[^A-Za-z0-9\s]", '', v))
            result[k] = current
    return result

# remove duplicate value list items
def unique_values(ls):
    result = dict()
    for key, value in ls.items():
        result[key] = list(set(value))
    return result

def main():
    merged_list = meerwoorden() + json_api_to_list()
    result = unique_values(list_values(merged_list))
    save_to_file(result)

if __name__ == '__main__':
    main()
