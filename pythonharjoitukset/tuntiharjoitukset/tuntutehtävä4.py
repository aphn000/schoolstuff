vuosi=int(input("Anna vuosi. "))

if vuosi >2026: print ("Vuosi on tulevaisuudessa.")
elif vuosi == 2021: print("Vuosi oli poikkeuksellisesti olympiavuosi.")
elif vuosi == 2020: print("Vuonna ei ollut olympialaisia poikkeuksellisesti. ")
elif vuosi %4 == 0: print("Vuosi on olympiavuosi.")
else:
    print("Vuosi ei ole olympiavuosi.")