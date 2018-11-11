def tah(pole, cislo_pole, symbol):
    return pole[:cislo_pole] + symbol + pole[cislo_pole + 1:]

print(tah("----", "c", "x"))
