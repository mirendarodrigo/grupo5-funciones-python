#tests/test_sumar.py 
from funciones.sumaCabral import sumar 

def test_sumar(): 
    assert sumar(3, 5) == 8
    assert sumar(-2, 2) == 0