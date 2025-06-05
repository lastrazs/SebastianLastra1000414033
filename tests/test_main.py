import pytest
from src.main import suma, resta, multiplicacion 
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(10, 10) == 0
    assert resta(-1, -1) == 0
    
def test_multiplicacion():
    assert multiplicacion(2, 3) == 6