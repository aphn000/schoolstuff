sukupuoli = input("Ilmoita biologinen sukupuoli: ")
hemoglobiini = int(input("Ilmoita hemoglobiiniarvo: "))

if sukupuoli == "nainen":
    if hemoglobiini >= 117 and hemoglobiini <= 175: print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiini >=175: print("Hemoglobiiniarvo on korkea.")
    elif hemoglobiini <=117: print("Hemoglobiiniarvo on alhainen")

elif sukupuoli == "mies":
    if hemoglobiini >= 134 and hemoglobiini <= 195: print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiini >=195: print("Hemoglobiiniarvo on korkea.")
    elif hemoglobiini <=134: print("Hemoglobiiniarvo on alhainen")
