def summa(lista):
    tulos=0

    for luku in lista:
        tulos=tulos+luku

    return tulos


luvut=[6, 7, 4, 20]
vastaus=summa(luvut)
print(vastaus)

