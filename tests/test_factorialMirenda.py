import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from funciones.factorialMirenda import factorial


def test_factorial():
    """Pruebas unitarias para la función factorial."""
    # Caso normal
    assert factorial(5) == 120

    # Caso con número negativo
    assert factorial(-3) is None
