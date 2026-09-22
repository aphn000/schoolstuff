class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        while self.kerros<kohde:
            self.kerros_ylos()

        while self.kerros>kohde:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros +=1
            print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1 
            print(f"Hissi on kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin, ylin, hissienmaara):
        self.hissit = []

        for i in range(hissienmaara):
            self.hissit.append(Hissi(alin,ylin))

    def aja_hissia(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)


h = Hissi (1, 10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

talo = Talo(1, 10, 3)

talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.aja_hissia(2, 3)

talo.aja_hissia(0, 1)
talo.aja_hissia(1, 1)
talo.aja_hissia(2, 1)

        

