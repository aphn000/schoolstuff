vuosi=int(input("Anna vuosi. "))

if vuosi >2026: print ("Vuosi on tulevaisuudessa.")
elif vuosi %4 == 0: print("Vuosi on olympiavuosi.")
elif vuosi == 2021: print("Vuosi on olympiavuosi.")
else:
    print("Vuosi ei ole olympiavuosi.")