class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.kuljettu_matka = 2000

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tuntimäärä):
        self.kuljettu_matka = self.kuljettu_matka+self.nopeus*tuntimäärä
    


auto1 = Auto("ABC-123", 142)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton nopeus: {auto1.nopeus} km/h")

auto1.kulje(1.5)

print (f"Kuljettu matka: {auto1.kuljettu_matka} km.")

auto1.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto1.nopeus} km/h")