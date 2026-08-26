import random

arvottunumero = random.randint(1, 10)
arvaus= 0

while arvottunumero != arvaus:
    arvaus = int(input("Arvaa luku väliltä 1-10.  "))

    if arvaus == arvottunumero:
        print("Arvasit oikean numeron.")
    elif arvaus >= arvottunumero:
        print ("Liian suuri arvaus.")
    elif arvaus <= arvottunumero:
        print("Liian pieni arvaus.")
    
    
