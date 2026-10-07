import json


TIEDOSTO = "saavutukset.json"

SAAVUUKSET =  {
    "ilmastonpelastaja": "Ilmaston pelastaja: tilasit kasvishampurilaisen.",
    "siivoaja": "Siivoaja: Siivosit roskia puistosta."
    "metsiensankari": "Metsien sankari: Pelastit metsän eläimet laittomilta hakkuilta"
}

def lataa():
    try:
        with open (TIEDOSTO) as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

def avaa (saavutus_id):
    avatut = lataa()
    if saavutus_id not in avatut:
        avatut.append(saavutus_id)
        with open (TIEDOSTO, "w") as f:
            json.dump(avatut, f)
        print("Sait saavutuksen: ", SAAVUUKSET[saavutus_id])

def nayta():
    avatut = lataa()
    print ("=== SAAVUTUKSET ===")
    for saavutus_id, kuvaus in SAAVUUKSET.items():
        if saavutus_id in avatut:
            print("[x]", kuvaus)
        else:
            print("[ ]???")

def syote(kysymys=""):
    vastaus = input(kysymys)
    while vastaus == "saavutukset":
        nayta()
        vastaus = input(kysymys)
    return vastaus