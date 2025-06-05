import pytest
from src.main import suma, resta, multiplicacion, division
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
def test_division():
    assert division(6, 3) == 2
    assert division(10, 2) == 5
    with pytest.raises(ValueError):
        division(5, 0)