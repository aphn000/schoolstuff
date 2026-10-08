import json

#tiedosto, johon saavutukset tallennetaan
TIEDOSTO = "saavutukset.json"

SAAVUUKSET =  {
    "ilmastonpelastaja": "Ilmaston pelastaja: tilasit kasvishampurilaisen.",
    "siivoaja": "Siivoaja: Siivosit roskia puistosta.",
    "metsiensankari": "Metsien sankari: Pelastit metsän eläimet laittomilta hakkuilta",
    "voittaja": "Voittaja: Voitit pelin ja pelastit maailman kaikelta pahalta"
}

def lataa():
    try:
        with open (TIEDOSTO) as f:
            return json.load(f)
        #avaa saavutustiedoston lukemiseen, muuttaa json tiedoston listaksi
    except FileNotFoundError:
        return[]
    #lataa saavutukset json tiedostosta

def avaa (saavutus_id):
    avatut = lataa()
    if saavutus_id not in avatut:
        avatut.append(saavutus_id)
        with open (TIEDOSTO, "w") as f:
            json.dump(avatut, f)
        print("Sait saavutuksen: ", SAAVUUKSET[saavutus_id])
        #funktio lisää pelaajalle uuden saavutuksen. Tarkistaa, onko saavutusta jo aiemmin saatu. Jos ei, lisää sen listaan.

def nayta():
    avatut = lataa()
    print ("=== SAAVUTUKSET ===")
    for saavutus_id, kuvaus in SAAVUUKSET.items():
        if saavutus_id in avatut:
            print("[x]", kuvaus)
        else:
            print("[ ], kuvaus")
#käy läpi saavutukset, jos saavutus on avattu: [x], jos ei niin [ ]
        

def syote(kysymys=""):
    vastaus = input(kysymys)
    while vastaus == "saavutukset":
        nayta()
        vastaus = input(kysymys)
    return vastaus