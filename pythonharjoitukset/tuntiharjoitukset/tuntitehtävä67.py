class Lentokone:
    def __init__(self, nimi, bensatankin_maksimi):
        self.nimi= nimi
        self.bensatankin_maksimi = bensatankin_maksimi
        self.bensatankin_nyk_lukema = 0

    def tankkaa(self):
        bensaa_mahtuu = self.bensatankin_maksimi - self.bensatankin_nyk_lukema
        self.bensatankin_maksimi = self.bensatankin_maksimi
    print (f"Bensatankkiin mahtuu {bensaa_mahtuu} litraa bensaa.")



    