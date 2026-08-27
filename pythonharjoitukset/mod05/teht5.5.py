print("Kerro salasana ja käyttäjätunnus.")

while kerrat < 5:
    kayttajatunnus = input("Anna käyttäjätunnus. ")
    salasana= (input("Anna salasana. "))
    if salasana == "rules" and kayttajatunnus == "python": 
        print("Tervetuloa!")
        break
    else: 
        print("Yritä uudelleen.")
        kerrat +=1
 else:
    print:("Pääsy evätty.")
 


    