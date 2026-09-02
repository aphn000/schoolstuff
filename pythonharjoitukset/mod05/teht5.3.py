lukujono = []

while True:
    luku=input("Anna luku.")
    lukujono.append (float(luku))
    if luku=="":
        break
    else:
        lukujono.append (float(luku))

print(lukujono, "Pienin", min, lukujono)
print(lukujono, "Isoin", max, lukujono)