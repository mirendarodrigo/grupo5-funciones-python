import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from funciones.dividir_vadala import dividir
def test_dividir():
 assert dividir(10, 2) == 5
 assert dividir(5, 0) is None
