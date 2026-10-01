class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.elossa = True

    def havisit(self, syy):
        print("Hävisit pelin!")
        print(syy)
        self.elossa = False