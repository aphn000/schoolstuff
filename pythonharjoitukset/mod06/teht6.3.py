luku = int((input)("Kerro kokolaisluku "))

yhdluku = False

if luku == 0 or luku == 1:
    print(luku, "ei ole alkuluku.")
elif luku > 1:
    for i in range(2, luku):
        if (luku % i) == 0:
            yhdluku = True
            break

  
    if yhdluku:
        print(luku, "ei ole alkuluku.")
    else:
        print(luku, "on alkuluku.")