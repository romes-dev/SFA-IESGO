import pytest 
from calculadora import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2,3) == 5
    assert somar(-1,1) == 0
    assert somar(0,0) == 0

def test_subtrair():
    assert subtrair(10,4) == 6
    assert subtrair(5,10) == -5

def test_multiplicar():
    assert multiplicar(3,4) == 12
    assert multiplicar(-2,5) == -10

def test_dividir():
    assert dividir(10,2) == 5
    assert dividir(9,3) == 3

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5,0)