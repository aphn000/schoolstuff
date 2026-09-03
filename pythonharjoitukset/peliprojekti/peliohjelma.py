nimi = input("Anna pelaajan nimi.")
ika = int(input("Anna pelaajan ikä."))

print("Pelaajan nimi: ", nimi)
print("Pelaajan ikä: ", ika)

while ika <12:
    print ("Olet alaikäinen ahahahahahh")
    break
else:
    print ("Hei ", nimi,"!")
    print ("Tervetuloa peliin.")
    print ("Voit seurata peliin liittyviä asioitasi päävalikossa. Komennolla PELAAJA saat tiedot pelaajastasi. Komennolla SAAVUTUKSET saat tiedot saamistasi saavutuksista. Komennolla LOPETA peli päättyy.")

paavalikko1 = "pelaaja".upper()
paavalikko2 = "saavutukset".upper()
paavalikko3 = "lopeta".upper()


while True:

    valinta = input("Kerro valintasi.")
    if valinta == paavalikko1:
        print("Pelaajan nimi on", nimi, "ja pelaajan ikä on", ika, ". Emme tiedä vielä muuta pelaajasta")
    elif valinta == paavalikko2: 
        print("Pelaajalla ei ole vielä saavutuksia, sillä peli on kehitysvaiheessa.")
    elif valinta == paavalikko3:
        print("Peli sammuu")
        break