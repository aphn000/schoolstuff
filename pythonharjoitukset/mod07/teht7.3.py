def muunnos_gallonoiksi (gallonat):
    return gallonat*3.785

gallonat= float(input("Anna gallonoiden määrä "))

while gallonat >=0:
    litrat=muunnos_gallonoiksi(gallonat)
    print (litrat, "litraa")

    gallonat= float(input("Anna gallonoiden määrä "))