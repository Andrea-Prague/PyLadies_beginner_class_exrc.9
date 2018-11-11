# Tohle je cely program pred rozdelenim, prepsala jsem par printu ve funkci piskvorky1d a input hodila to volani ve fci piskovrky1d namisto
#  volani v tahu hrace, ale jinak nevidim moznost, kde to zkratit, tak aby se program nerozbil, nemate nejakiou radu?

from random import randrange

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_pole, symbol):
    return pole[:cislo_pole] + symbol + pole[cislo_pole + 1:]


def tah_hrace (pole, cislo_pole):
    while True:
        if cislo_pole <0:
            print ("nelze zadat zaporne cislo, zkus to znovu")
        elif cislo_pole > len(pole)-1:
            print ("moc vysoke cislo, zkus to znovu")
        elif "-" not in pole[cislo_pole]:
            print ("toto pole je obsazene, zkus to znovu")
        else:
            return tah(pole, cislo_pole,"x")

def tah_pocitace(pole):
    pc_cislo_pole = randrange(len(pole))
    while not "-" in pole[pc_cislo_pole]:
        pc_cislo_pole = randrange(len(pole))
    return tah (pole, pc_cislo_pole, "o")

def piskovrky1d():
    pole = "-" * 20
    while "-" in pole:
            pole = tah_hrace(pole, int (input ("zadej cislo pole, kde chces udelat tah ")))

            if vyhodnot(pole) == "x":
                print (pole)
                return ("uzivatel vyhral")
                break

            pole = tah_pocitace(pole)
            print (pole)

            if vyhodnot(pole) == "o":
                return ("PC vyhral")
                break

    if vyhodnot(pole) == "!":
        return ("remiza")

print (piskovrky1d())
