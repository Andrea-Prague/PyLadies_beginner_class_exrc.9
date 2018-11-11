import pytest
import ai
from piskvorky import tah, vyhodnot, tah_hrace
from random import randrange

pole = "-"*5

# zjisti, zda se vypisuje tah pocitace, konkretne znakem "o"
def test_tah_pocitace_v_poli():
    assert "o" in ai.tah_pocitace(pole)

# kontroluje, ze pocitac nevyuziva znak "x", ale pokud by bylo vic kol(v poli uz tahy hrace), pak by tento test nefungoval?
def test_pocitac_spatny_znak():
    assert "x" not in ai.tah_pocitace(pole)

# testuje fci vyhodnot, zda prirazuje spravne hodnoceni v pripade tahu hrace
def test_vyhodnot_x():
    assert vyhodnot("xxx") == "x"

# pro pole, ktere nema zadne tahy se vraci ve vyhodnot pole
def test_vyhodnot():
    assert vyhodnot(pole) == "-"

# kontroluje, zda se tahy prirazuji spravemu poli
def test_spravny_tah():
    assert tah(pole, 3, "x") == "---x-"

# pokud bude tah stringem, vyhodi to TypeError
def test_spatny_tah():
    with pytest.raises(TypeError):
        tah(pole, "str", "x")
