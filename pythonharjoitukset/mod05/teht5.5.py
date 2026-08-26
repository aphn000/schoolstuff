print("Kerro salasana ja käyttäjätunnus.")
kerrat = 0

while kerrat < 5:
    kayttajatunnus = input("Anna käyttäjätunnus. ")
    salasana= (input("Anna salasana. "))
    if salasana == "rules" and kayttajatunnus == "python": 
        print("Tervetuloa!")
        break
    else: 
        print("Pääsy evätty. Yritä uudelleen.")
        kerrat +=1

    