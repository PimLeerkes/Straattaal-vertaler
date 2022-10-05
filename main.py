

#vertaald woord op basis van richting in talen en beschikbare woordenboek
def vertaal_woord(woord, richting, woorden):
    vertaald_woord = ""
    for i, j in enumerate(woorden):
        if str.upper(j) == str.upper(woord):
            if int(richting) == 1:
                vertaald_woord = woorden[i+1]
            elif int(richting) == 2:
                vertaald_woord = woorden[i-1]
    return vertaald_woord


def main():
    print("Welkom bij straattaalvertaler versie 0.0.1!")
    print("Maak geen spellingsfouten bij het vertalen maar hoofdletters maken niet uit.")
    print("")

    #laad de woorden in een list (woordenboek):
    woorden = open("woorden.txt", "r")
    woorden = woorden.readlines()
    res = []
    for w in woorden:
        woord = w.replace("\n", "")
        woord = woord.replace("\t", "")
        woord = woord.replace('id', "")
        woord = woord.replace('woord', "")
        woord = woord.replace('betekenis', "")
        woord = woord.replace('"', "")
        if len(woord) > 4:
            res.append(woord)

    #vraag om woorden te vertalen en print resultaat:
    while(True):
        richting = input("Wil je van nederlands naar straattaal? (1) of van straattaal naar nederlands? (2): ")
        woord = input("Welk woord of zin wil je vertalen?: ")
        vertaalde_woord = vertaal_woord(woord, richting, res)
        print("De vertalling voor: '" + woord + "' is: " + vertaalde_woord)
        print("")


if __name__ == '__main__':
    main()

