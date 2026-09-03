import random

lukumaara = int(input("Kerro arpakuutioiden lukumäärä "))
summa = 0

for i in range(lukumaara):
    print ("Heitetään arpakuutio.")
    silmaluku = random.randint(1,6)
    summa=summa+silmaluku
print("Silmälukujen summa on", summa)
