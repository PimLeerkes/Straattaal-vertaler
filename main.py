from pprint import pprint
import json

class Woordenboek(dict):

    def __init__(self):
        self = dict()

    # voeg woord toe:
    def add(self, key, value):
        self[str.upper(key)] = value

    # laat alle woorden zien:
    def show(self):
        print(self)

    # vertaalt woord:
    def vertaal(self, key):
        if str.upper(key) in self:
            return str.lower(self[str.upper(key)])
        else:
            return str.lower(key)


# iterate door de zin en vertaald elk woord los van elkaar:
def vertaal_zin(zin, woorden):
    zin = zin.split()
    # split de zin eerst in mogelijke subzinnen
    #subzinnen = []
    #for i in range(len(zin)):
    #    for j in range(i, len(zin)):
    #        subzin = zin[i:j]
    #        nieuw_subzin = ""
    #        for woord in subzin:
    #            nieuw_subzin = nieuw_subzin + " " + woord
    #        subzinnen.append(nieuw_subzin[1:])
    #print(subzinnen)

    # vertaal de losse subzinnen:
    #nieuwe_subzinnen = []
    #for subzin in subzinnen:
    #    nieuw_subzin = vertaal_woord(subzin, richting, woorden)
    #    subzin = nieuw_subzin
    #    nieuwe_subzinnen.append(subzin)
    #return nieuwe_subzinnen


    nieuwe_zin = ""
    for woord in zin:
        nieuw_woord = woorden.vertaal(woord)
        if nieuw_woord != "":
            woord = nieuw_woord
        nieuwe_zin = nieuwe_zin + " " + woord
    return nieuwe_zin


def main():
    print("Welkom bij straattaalvertaler versie 0.0.4!")
    print("Maak geen spellingsfouten bij het vertalen maar hoofdletters maken niet uit.")
    print("")

    #laad de woorden in 2 woordenboeken. 1 van nederlands naar straattaal en 1 andersom.:

    # laad de "test.json" gemaakt door api request in get-data.py
    with open("woorden.json", "r") as data:
        woorden = json.load(data)
        ned_str, str_ned = Woordenboek(), Woordenboek()
        for woord in woorden:
            ned_woord = woord["betekenis"]
            str_woord = woord["woord"]
            ned_str.add(ned_woord, str_woord)
            str_ned.add(str_woord, ned_woord)

    # vraag om woorden te vertalen en print resultaat:
    while(True):
        richting = input("Wil je van nederlands naar straattaal? (1) of van straattaal naar nederlands? (2): ")
        if richting == "1":
            woordenlijst = ned_str
        elif richting == "2":
            woordenlijst = str_ned
        else:
            print("Vul 1 of 2 in alstjeblieft. Dit mag niet!!!")
            continue

        zin = input("Welk woord of zin wil je vertalen?: ")
        vertaalde_zin = list(vertaal_zin(zin, woordenlijst))
        vertaalde_zin[1] = str.upper(vertaalde_zin[1])
        vertaalde_zin = "".join(vertaalde_zin)
        print("")
        print("De vertaling voor: '" + zin + "' is: " + vertaalde_zin + ".")
        print("")

if __name__ == '__main__':
    main()
