class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    def havisit(self, syy):
        print("Hävisit pelin!")
        print(syy)
