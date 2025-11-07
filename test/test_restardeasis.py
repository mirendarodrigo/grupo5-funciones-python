import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from funciones.restardeasis import restar

def test_restar():
 assert restar(10, 4) == 6
 assert restar(5, 10) == -5