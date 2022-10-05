
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


# iterate door de zin en vertaald elk woord los van elkaar:
def vertaal_zin(zin, richting, woorden):

    # split de zin eerst in mogelijke subzinnen
    #zin = zin.split()
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
        nieuw_woord = vertaal_woord(woord, richting, woorden)
        if nieuw_woord != "":
            woord = nieuw_woord
        nieuwe_zin = nieuwe_zin + " " + woord
    return nieuwe_zin


def main():
    print("Welkom bij straattaalvertaler versie 0.0.3!")
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
        if woord != "" and woord[len(woord)-1] == " ":
            woord = woord[:-1]
        res.append(woord)

    #vraag om woorden te vertalen en print resultaat:
    while(True):
        richting = input("Wil je van nederlands naar straattaal? (1) of van straattaal naar nederlands? (2): ")
        zin = input("Welk woord of zin wil je vertalen?: ")
        vertaalde_woord = vertaal_zin(zin, richting, res)
        print("")
        #print(vertaalde_woord)
        print("De vertaling voor: '" + zin + "' is: " + vertaalde_woord)
        print("")


if __name__ == '__main__':
    main()


