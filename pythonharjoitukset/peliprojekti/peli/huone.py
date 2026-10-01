class Huone:
    def __init__(self, nimi):
        self.nimi = nimi

    def saavu(self):
        print("Saavuit paikkaan: {self.nimi}")

    koti = Huone("Koti")
    hesburger = Huone("Hesburger")
    puisto = Huone("Puisto")

