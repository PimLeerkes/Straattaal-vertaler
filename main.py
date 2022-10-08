from pprint import pprint
import json
import random

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
            print(woord)
            vertaald_woord = str.upper(vertaald_woord[0]) + vertaald_woord[1:]

        return vertaald_woord



# seperate het woord van omliggende punten, kommas etc.
def leestekens(woord, woorden):

    left = ''
    right = ''
    if woorden.vertaal(woord) == woord and len(woord) > 1:
        while woord[0] not in allowed:
            left = left + woord[0]
            woord = woord[1:] 
        while woord[len(woord)-1] not in allowed:
            right = right + woord[len(woord)-1]
            woord = woord[:-1]
    return left, woord, right



# iterate door de zin en vertaald elk woord of zinsdeel los van elkaar:
def vertaal_zin(zin, woorden):
    zin = zin.split()
    vertaalde_zin = ""

    #we lopen door elk woord van de zin heen en nemen ze als begin punt:
    i = 0
    while i < len(zin) and i < 10:
        #vertaal het woord:
        woord = zin[i]
        left, woord, right = leestekens(woord, woorden)
        vertaald_woord = left + woorden.vertaal(woord) + right
  
        #voor elk volgende woord plak het erachteraan en vertaal ze als een zinsdeel:
        langer_woord = woord
        for j in range(i, len(zin)-1):
            #vertaal het stuk wat je krijgt als je een woord toevoegt:
            langer_woord = langer_woord + " " + zin[j+1]
            left, langer_woord, right = leestekens(langer_woord, woorden)
            langer_vertaald_woord = woorden.vertaal(langer_woord)

            #als het een nieuwe vertaling geeft dan houden we bij dat we daar waren gebleven.
            if woorden.vertaal(langer_woord) != langer_vertaald_woord:
                vertaald_woord = left + langer_vertaald_woord + right
                i = j + 1

        vertaalde_zin = vertaalde_zin + " " + vertaald_woord
        i = i + 1


    return vertaalde_zin[1:]


def main():
    print("Welkom bij straattaalvertaler versie 0.0.9!")

    #laad de woorden in 2 woordenboeken. 1 van nederlands naar straattaal en 1 andersom.:

    # laad de "test.json" gemaakt door api request in get-data.py
    with open("woorden.json", "r") as data:
        woorden = json.load(data)
        ned_str, str_ned = Woordenboek(), Woordenboek()
        for woord in woorden:
            for key, val in woord.items():
                str_ned.add(key, val)
                ned_str.add(val, key)


    # voegt de woorden uit meerwoorden.txt ook toe aan de woordenboeken:
    with open("meerwoorden.txt", "r") as data:
        for woord in data:
            woord = woord.split("=")
            woord[1] = woord[1].replace("\n","")
            woord[0] = woord[0].split(",")
            woord[1] = woord[1].split(",")
            for w in woord[1]:
                str_ned.add(w, woord[0])
            for v in woord[0]:
                ned_str.add(v, woord[1])


    # vraag om woorden te vertalen en print resultaat:
    richting = input("Wil je van nederlands naar straattaal? (1) of van straattaal naar nederlands? (2): ")
    while True:
        if richting == "1":
            woordenlijst = ned_str
        elif richting == "2":
            woordenlijst = str_ned
        else:
            print("Vul 1 of 2 in alstjeblieft. Dit mag niet!!!")
            continue

        zin = input("Welk woord of zin wil je vertalen?: ")
        vertaalde_zin = vertaal_zin(zin, woordenlijst)
        print("\nDe vertaling voor: '" + zin + "' is:\n" + vertaalde_zin + "\n")


if __name__ == '__main__':
    main()
