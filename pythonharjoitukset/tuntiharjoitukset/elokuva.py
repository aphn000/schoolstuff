while True:
    tiedoston_nimi=input("Kerro tiedoston nimi.")
    try:
        with open (tiedoston_nimi, "r") as tiedosto:
            data = tiedosto.read()
            print(data)
            break
    except FileNotFoundError:
        print("Tiedostoa ei löydy://")