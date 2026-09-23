class Julkaisu:
    def __init__(self, julkaisu_nimi):
        self.julkaisu_nimi = julkaisu_nimi


class Kirja(Julkaisu):
    def __init__(self, julkaisu_nimi, kirjoittaja, sivumaara):
        super().__init__(julkaisu_nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print (f"Kirjan nimi on {self.julkaisu_nimi}")
        print (f"Kirjan kirjoittaja on {self.kirjoittaja}")
        print (f"Kirjan sivumäärä on {self.sivumaara}")

class Lehti(Julkaisu): 
    def __init__(self, julkaisu_nimi, paatoimittaja):
        super().__init__(julkaisu_nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.julkaisu_nimi}")
        print(f"Päätoimittaja on {self.paatoimittaja}")
    

hytti = Kirja("Hytti n:o 6", "Rosa Liksom", "200")
akuankka = Lehti("Aku Ankka", "Aku Hyyppä")

hytti.tulosta_tiedot()

akuankka.tulosta_tiedot()
