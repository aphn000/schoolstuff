
from peliprojektikorjaus.seikkailupeli.pelaaja import Pelaaja
from peliprojektikorjaus.seikkailupeli.huone import Huone
from peliprojektikorjaus.seikkailupeli.valikko import valinta

def aloita_peli():


    print("Tervetuoloa seikkailupeliin.")
    print("Tässä pelissä sinun täytyy viettää mukava vapaapäivä.")
    print("Mutta se ei olekaan niin yksinkertaista...")
    print("Sinun täytyy tehdä kestävää kehitystä edesajavia ratkaisuja edetäksesi pelissä.")
    
    

    nimi = input("Anna pelaajan nimi.")
    ika = int(input("Anna pelaajan ikä."))

    pelaaja = Pelaaja(nimi,ika)

    print("Pelaajan nimi: ", nimi)
    print("Pelaajan ikä: ", ika)

    if ika <12:
        print ("Olet alaikäinen ahahahahahh")
        return
    else:
        print("Hei ", nimi, "!")
        print("Tervetuloa peliin.")
    
  #  print("Voit seurata peliin liittyviä asioitasi päävalikossa.")
   # print("Komennolla LISÄÄ voit lisätä esineitä pelaajasi tavaraluetteloon.")
    #print("Komennolla TAVARALUETTELO voit tarkastella pelaajasi tavaraluetteloa.")
    #print("Komennolla APUA saat ohjeita pelin toimintaan.")
    #print("Komennolla LOPETA peli päättyy.")

#esineet = []

#def lisaa_esine():
 #   esine = input("Kerro, minkä esineen haluat antaa pelaajallesi.")
  #  esineet.append(esine)
   # print("Esine on lisätty tavaraluetteloon.")


#def nayta_esineet():
 #   print("Pelaajallasi on seuraavat esineet")

  #  for esine in esineet:
   #     print(esine)

#def apua():
 #   print("LISÄÄ = lisää esine tavaraluetteloon")
  #  print("TAVARALUETTELO = näyttää pelaajan tavaraluettelon")
   # print("APUA = näyttää pelin ohjeet")
    #print("LOPETA = lopettaa pelin ja sulkee ohjelman")


#paavalikko1 = "LISÄÄ".upper()
#paavalikko2 = "TAVARALUETTELO".upper()
#paavalikko3 = "APUA".upper()
#paavalikko4 = "LOPETA".upper()


#while True:

 #   valinta=input("Kerro valintasi.").upper()

 #   if valinta == paavalikko1:
  #      lisaa_esine()
   # elif valinta == paavalikko2:
        #nayta_esineet()
    #elif valinta == paavalikko3:
        #apua()
    #elif valinta == paavalikko4:
     #   print("Peli sammuu")
      #  break

    koti = Huone("Koti")
    hesburger = Huone("Hesburger")
    puisto = Huone("Puisto")
    

    koti.saavu()

    print("Heräät aamulla nälkäisenä ja kaipaat jotain rasvaista")

    input("Paina Enter jatkaaksesi pelissä")

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

    else:
        print("Virheellinen valinta, valitse 1 tai 2.")
        return

    input("Paina Enter jatkaaksesi pelissä")

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
    else:
        print("Virheellinen valinta, valitse 1 tai 2.")
        return

    

if __name__ == "__main__":
    aloita_peli()
