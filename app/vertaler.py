from pprint import pprint
import json
import random
import sys

allowed = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L',
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

class Woordenboek(dict):

    def __init__(self):
        self = dict()

    # voeg woord toe:
    def add(self, key, value):
        self[str.upper(key)] = value

    # laat alle woorden zien:
    def show(self):
        for key, value in self.items():
            print("woord: " + key + " vertaling: " + str(value))

    # vertaalt woord:
    def vertaal(self, woord):
        
        #gaat langs alle woorden en slaat elke instantie op in synoniemen. kiest hier een random uit:
        vertaald_woord = str.lower(woord)
        synoniemen = []
        for key, value in self.items():
            if key == str.upper(woord) and type(value) == list:
                synoniemen = synoniemen + value
            elif key == str.upper(woord):
                synoniemen.append(value)  
        if len(synoniemen) > 0:
            vertaald_woord = random.choice(synoniemen)

        #als een woord in volledig caps gegeven wordt returnen we hem ook zo:
        if woord.isupper():
            vertaald_woord = str.upper(vertaald_woord)

        #als een woord begint met hoofdletter returnen we m ook zo:
        if woord[0].isupper():
            vertaald_woord = str.upper(vertaald_woord[0]) + vertaald_woord[1:]

        return vertaald_woord


# hendelt alles met leestekens.
def leestekens(woord, woorden):

    #haalt de leestekens eraf en slaat ze op in leestekens:
    tekens = ''
    if woorden.vertaal(woord) == woord and len(woord) > 1:
        #het gaat in een loop omdat er bijvoorbeeld meerdere vraagtekens kunnen staan achter elkaar:
        while woord[len(woord)-1] not in allowed:
            tekens = tekens + woord[len(woord)-1]
            woord = woord[:-1]

    #todo: als een woord zonder vraagteken ineens geen vertaling geeft en met wel willen we alsnog dat ie vertaalt:        
    #if woorden.vertaal(woord) == woord and woorden.vertaal(woord + "?") != woord:
    #    woord = woord + "?"

    #todo: vraagteken alsnog erachteraan plakken als het originele woord het wel heeft en de vertaling niet zoals bij: 
    # alles goed? -> wassup

    return woord, tekens



# iterate door de zin en vertaald elk woord of zinsdeel los van elkaar:
def vertaal_zin(zin, woorden):
    zin = zin.split()
    vertaalde_zin = ""

    #we lopen door elk woord van de zin heen en nemen ze als begin punt:
    i = 0
    while i < len(zin) and i < 10:
        #vertaal het woord:
        woord = zin[i]
        woord, tekens = leestekens(woord, woorden)
        vertaald_woord = woorden.vertaal(woord) + tekens
  
        #voor elk volgende woord plak het erachteraan en vertaal ze als een zinsdeel:
        langer_woord = woord
        for j in range(i, len(zin)-1):
            #vertaal het stuk wat je krijgt als je een woord toevoegt:
            langer_woord = langer_woord + " " + zin[j+1]
            langer_woord, tekens = leestekens(langer_woord, woorden)
            langer_vertaald_woord = woorden.vertaal(langer_woord)

            #als het een nieuwe vertaling geeft dan houden we bij dat we daar waren gebleven.
            if str.lower(langer_woord) != str.lower(langer_vertaald_woord):
                vertaald_woord = langer_vertaald_woord + tekens
                i = j + 1

        vertaalde_zin = vertaalde_zin + " " + vertaald_woord
        i = i + 1

    return vertaalde_zin[1:]


def laad_woorden():
    with open("./app/data/woorden.json", "r") as data:
        woorden = json.load(data)
        ned_str = Woordenboek()
        for key, val in woorden.items():
            ned_str.add(key, val)
    return ned_str

def main(zin):
    woordenlijst = laad_woorden()
    vertaalde_zin = vertaal_zin(zin, woordenlijst)
    return vertaalde_zin
