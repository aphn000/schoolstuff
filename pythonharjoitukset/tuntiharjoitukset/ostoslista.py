with open ("ostoslista.txt", "w") as tiedosto:
    tiedosto.write("maito\n")
    tiedosto.write("leipä\n")
    tiedosto.write("kananmunat\n")
with open ("ostoslista.txt", "a") as tiedosto:
    tiedosto.write("omena\n")

with open ("ostoslista.txt", "r") as tiedosto:
    sisalto = tiedosto.read()
    print(sisalto)
    rivit = tiedosto.readlines()
    print(rivit)