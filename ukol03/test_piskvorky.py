import pytest
import ai

from random import randrange

pole = "-"*5

def test_symbol_pc():
    assert "o" in ai.tah_pocitace(pole, "o")
