print("Valitse laskutoimitus: PLUS, MIINUS, KERTOLASKU, tai LOPETUS")
valitse=input("Kerro valintasi.")

valinta_1="PLUS"
valinta_2="MIINUS"
valinta_3="KERTOLASKU"
valinta_4="LOPETUS"

num1=float(input("Kerro ensimmäinen numero"))
num2=float(input("Kerro toinen numero"))

while valitse:
    if valinta_1:
        print("Summa on", num1+num2)
    elif valinta_2:
        print("Summa on", num1-num2)
    elif valinta_3:
        print("Summa on", num1*num2)
    elif valinta_4:
        print("Lopetit laskemisen")
else:
    break
    

    