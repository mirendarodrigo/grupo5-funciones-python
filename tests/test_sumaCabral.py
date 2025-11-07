#tests/test_sumar.py 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from funciones.sumaCabral import sumar 

def test_sumar(): 
    assert sumar(3, 5) == 8
    assert sumar(-2, 2) == 0