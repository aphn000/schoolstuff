def poista_parittomat(lista):
    parillinenlista = []
    for numero in lista:
        if lasku == 0:
            parillinenlista.append(numero)
        return parillinenlista

lista= [1,7,9,13,12,24]
tulos= poista_parittomat()
print (tulos)