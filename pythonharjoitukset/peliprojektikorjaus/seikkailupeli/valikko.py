def valinta(vaihtoehdot):
    for numero, vaihtoehto in enumerate(vaihtoehdot,1):
        print(f"{numero}.{vaihtoehto}")

    return input ("Valintasi on ")