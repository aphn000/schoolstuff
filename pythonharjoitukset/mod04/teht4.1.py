kuhanmitta = float(input("Anna kuhan mitta. "))

if kuhanmitta <=37:
    puuttuva_pituus = 37-kuhanmitta
    print("Laske kuha takaisin veteen.")
    print("Kuhan pituudesta puuttuu", puuttuva_pituus, "cm.")
elif kuhanmitta >=37:
    print("Voit pitää kuhan.")

