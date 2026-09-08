import random

def nopanheitto():
    silmaluku = random.randint(1,6)
    return silmaluku

silmaluku = nopanheitto()

while silmaluku != 6:
    print (silmaluku)
    silmaluku = nopanheitto()

print (silmaluku)
