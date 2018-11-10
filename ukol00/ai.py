from random import randrange
# from piskvorky import tah

def tah_pocitace(pole):
    pc_cislo_pole = randrange(len(pole))
    while not "-" in pole[pc_cislo_pole]:
        pc_cislo_pole = randrange(len(pole))
    return tah (pole, pc_cislo_pole, "o")
