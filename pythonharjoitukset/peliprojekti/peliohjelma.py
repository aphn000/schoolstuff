nimi = input("Anna pelaajan nimi.")
ika = int(input("Anna pelaajan ikä."))

print("Pelaajan nimi: ", nimi)
print("Pelaajan ikä: ", ika)

while ika <12:
    print ("Olet alaikäinen ahahahahahh")
    break
else:
    print("Hei ", nimi, "!")
    print("Tervetuloa peliin.")
    print("Voit seurata peliin liittyviä asioitasi päävalikossa.")
    print("Komennolla LISÄÄ voit lisätä esineitä pelaajasi tavaraluetteloon.")
    print("Komennolla TAVARALUETTELO voit tarkastella pelaajasi tavaraluetteloa.")
    print("Komennolla APUA saat ohjeita pelin toimintaan.")
    print("Komennolla LOPETA peli päättyy.")

esineet = []

def lisaa_esine():
    esine = input("Kerro, minkä esineen haluat antaa pelaajallesi.")
    esineet.append(esine)
    print("Esine on lisätty tavaraluetteloon.")


def nayta_esineet():
    print("Pelaajallasi on seuraavat esineet")

    for esine in esineet:
        print(esine)

def apua():
    print("LISÄÄ = lisää esine tavaraluetteloon")
    print("TAVARALUETTELO = näyttää pelaajan tavaraluettelon")
    print("APUA = näyttää pelin ohjeet")
    print("LOPETA = lopettaa pelin ja sulkee ohjelman")


paavalikko1 = "LISÄÄ".upper()
paavalikko2 = "TAVARALUETTELO".upper()
paavalikko3 = "APUA".upper()
paavalikko4 = "LOPETA".upper()


while True:

    valinta=input("Kerro valintasi.").upper()

    if valinta == paavalikko1:
        lisaa_esine()
    elif valinta == paavalikko2:
        nayta_esineet()
    elif valinta == paavalikko3:
        apua()
    elif valinta == paavalikko4:
        print("Peli sammuu")
        break