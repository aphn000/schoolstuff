import random

maksimi = int(input("Kuinka monta tahkoa nopassa?"))

def nopanheitto(tahkojen_maara):
    return random.randint(1,tahkojen_maara)
    

silmaluku = nopanheitto(maksimi)

while silmaluku != maksimi:
    print (silmaluku)
    silmaluku = nopanheitto(maksimi)

print (silmaluku)
