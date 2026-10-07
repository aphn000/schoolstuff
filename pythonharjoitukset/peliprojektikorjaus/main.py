from peliprojektikorjaus.seikkailupeli.pelaaja import Pelaaja
from peliprojektikorjaus.seikkailupeli.huone import Huone
from peliprojektikorjaus.seikkailupeli.valikko import valinta
from peliprojektikorjaus.seikkailupeli import saavutukset
from peliprojektikorjaus.seikkailupeli.saavutukset import syote
import os

def lue_tiedosto(tiedostonimi):
    polku = os.path.join(os.path.dirname(__file__), tiedostonimi)

    with open(polku, "r", encoding="utf-8") as tiedosto:
        return tiedosto.read()

def tallenna_peli(pelaaja, vaihe):
    polku = os.path.join(os.path.dirname(__file__), "tallennus.txt")

    with open(polku, "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(str(pelaaja.ika) + "\n")
        tiedosto.write(str(vaihe) + "\n")

def lataa_peli():
    polku = os.path.join(os.path.dirname(__file__), "tallennus.txt")

    try:
        with open(polku, "r", encoding="utf-8") as tiedosto:
            nimi = tiedosto.readline().strip()
            ika = int(tiedosto.readline().strip())
            vaihe = int(tiedosto.readline().strip())

        return nimi, ika, vaihe

    except FileNotFoundError:
        return None

def paavalikko():
    while True:
        print ("\nViikonloppu-seikkailupeli")
        print("1. Aloita peli.")
        print("2. Katso saavutukset")
        print("3. Katso pelaajan tiedot")
        print("4. Lopeta peli")      

        valinta = input("Valitse: ")

        if valinta == "1":
            aloita_peli()
        elif valinta == "2":
            saavutukset.nayta()
        elif valinta == "3":
            tallennettu_peli = lataa_peli()

            if tallennettu_peli is not None:
                nimi, ika, vaihe = tallennettu_peli

                print("\nPELAAJAN TIEDOT")
                print("Nimi:", nimi)
                print("Ikä:", ika)
                print("Pelin vaihe:", vaihe)

            else:
                print("\nPelaasta ei löytynyt tallennusta.")

        elif valinta == "4":
            print("Lopetit pelin")
            break

        else:
            print ("Virheellinen valinta. Valitse 1-4.")     

def aloita_peli():

    print(lue_tiedosto("intro.txt"))
    print()
    print(lue_tiedosto("ohjeet.txt"))

    tallennettu_peli = lataa_peli()

    if tallennettu_peli is not None:
        print("Tallennettu peli löytyi.")
        jatka = input("Haluatko jatkaa peliä? Vastaa joko kyllä tai ei. ")

        if jatka == "kyllä":
            nimi, ika, vaihe = tallennettu_peli

            print ("Tervetuloa takas peliin ", nimi)

        else:
            nimi = syote("Anna pelaajan nimi.")
            ika = int(input("Anna pelaajan ikä."))
            vaihe = 1

    else:
        nimi = syote("Anna pelaajan nimi.")
        ika = int(input("Anna pelaajan ikä."))
        vaihe = 1
    pelaaja = Pelaaja(nimi, ika) 

    print("Pelaajan nimi: ", nimi)
    print("Pelaajan ikä: ", ika)

    if ika <12:
        print ("Olet alaikäinen ahahahahahh")
        return
    else:
        print("Hei ", nimi, "!")
        print("Tervetuloa peliin.")
    
    koti = Huone("Koti")
    hesburger = Huone("Hesburger")
    puisto = Huone("Puisto")
    metsa = Huone("Metsä")
    taisteluareena = Huone("taisteluareena")

    if vaihe == 1:

        koti.saavu()

        print("Heräät aamulla nälkäisenä ja kaipaat jotain rasvaista")
        print ("Päätät lähteä Hesburgeriin syömään hampurilaista")

        syote("Paina Enter jatkaaksesi pelissä")

        tallenna_peli(pelaaja, 2)
        vaihe = 2

    if vaihe == 2:

        hesburger.saavu()

        print("Menet tilaamaan ruokaa.")
        print("Sinun tekee mieli kerroshampurilaista, mutta olet myös huolissasi ilmastonmuutoksesta.")
        print("Nyt sinun täytyy valita tarkkaan, otatko kasvis- vai lihavaihtoehdon. Lihassa hiilijalanjälki on paljon suurempi.")

        pelaajan_valinta = valinta(["Kerroshampurilainen","Kasvishampurilainen"])

        if pelaajan_valinta == "1":
            pelaaja.havisit("Tunsit ilmastoahdistusta ja hävisit pelin")
            return

        elif pelaajan_valinta == "2":
            print("Teit oikean päätöksen ottaessasi kasvishampurilaisen.")
            print("Pääset jatkamaan peliä!")
            saavutukset.avaa("ilmastonpelastaja")

            syote("Paina Enter jatkaaksesi pelissä")

            vaihe = 3
            tallenna_peli(pelaaja, 3)

        else:
            print("Virheellinen valinta, valitse 1 tai 2.")
            return

    if vaihe == 3:

        puisto.saavu()

        print("Näet kun joku tiputtaa roskan maahan puistossa.")
        print("Nyt sinun täytyy tehdä tärkeä valinta.")
        print("Valitse, aiotko heittää roskan roskiin vai jätätkö sen maahan.")

        pelaajan_valinta = valinta(["Vien roskan roskiin", "Jätän roskan maahan"])

        if pelaajan_valinta == "2":
            pelaaja.havisit("Kompastuit kävellessäsi banaaninkuoreen ja hävisit pelin")
            return
        elif pelaajan_valinta == "1":
            print("Teit oikean valinnan, onneksi olkoon.")
            print("Pääset jatkamaan peliä")
            saavutukset.avaa("siivoaja")

            syote("Paina Enter jatkaaksesi pelissä")

            vaihe = 4
            tallenna_peli(pelaaja, 4)
            
        else:
            print("Virheellinen valinta, valitse 1 tai 2.")
            return

    if vaihe == 4:

        metsa.saavu()

        print("Päätit mennä kansallispuistoon kävelemään ja nauttimaan Suomen uniikista luonnosta.")
        print("Näet kuitenkin jotain kummaa.")
        print("Metsäkoneet kaatavat hehtaareittain metsää laitonta datakeskusta varten.")
        print("Nyt sinun täytyy valita, soitatko poliisit vai et.")

        pelaajan_valinta = valinta(["Soitan poliisit", "Annan heidän jatkaa hakkuita" ])

        if pelaajan_valinta == "2":
            pelaaja.havisit("Laittomat hakkuut veivät rauhoitetulta eläinlajilta elinpaikan.")
            return

        elif pelaajan_valinta == "1":
            print("Teit oikean valinnan")
            print("Metsän eläimet kiittävät sinua vastuullisesta teosta")
            saavutukset.avaa("metsiensankari")
            syote("Paina enter jatkaaksesi pelisssä")

            vaihe = 5
            tallenna_peli(pelaaja, 5)
            
        else: 
            print("Virheellinen valinta, valitse 1 tai 2")
            return

    if vaihe == 5:

        taisteluareena.saavu()

        print("Olet saanut pidettyä elintapasi hyvin kestävän kehityksen mukaisina.")
        print("Sinulla on kuitenkin vielä yksi vihollinen, aiemmin puistossa kohtaamasi roskaaja.")
        print("Sinun on nyt valittava tarkkaan, jätätkö hänet rauhaan, heität häntä roskapussilla kostoksi vai kätteletkö häntä ja vältät konfliktin.")

        pelaajan_valinta = valinta(["Jätän hänet rauhaan", "Heitän häntä roskapussilla", "Kättelen häntä"])

        if pelaajan_valinta == "1":
            pelaaja.havisit("Hän pääsi jatkamaan roskaamista ja pilasi Suomen luonnon.")
            return

        elif pelaajan_valinta == "2":
            pelaaja.havisit("Jouduit konfliktiin ja hän heitti sinut roskapönttöön, johon jäit jumiin.")
            return

        elif pelaajan_valinta == "3":
            print("Vältit konfliktin, sekä pääsit puhumaan järkeä roskaajan päähän. Hän lopetti roskaamisen")
            print("Voitit pelin, onneksi olkoon.")
            saavutukset.avaa("voittaja")
        else:
            print("virheellinen valinta, valitse 1, 2 tai 3.")
            return

if __name__ == "__main__":
    paavalikko()
