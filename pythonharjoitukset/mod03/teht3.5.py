leiviska = float(input("Anna leiviskät"))
naula = float(input("Anna naulat"))
luoti = float(input("Anna luodit"))

luotienpaino = luoti*13.3
naulojenpaino = naula*32*13.3
leiviskoidenpaino = leiviska*20*32*13.3

yhteispaino = luotienpaino + naulojenpaino + leiviskoidenpaino

kilot = yhteispaino//1000
grammat = yhteispaino%1000

print("Massa nykymittojen mukaan", kilot, "kilogrammaa ja", grammat, "grammaa.")