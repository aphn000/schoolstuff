import random


N=int(input("Kerro kulmapisteiden määrä."))

i = 0
n = 0

while i < N:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    i += 1

piin_arvo = 4 * n / N

print("Piin likiarvo on", piin_arvo)