# tests/test_utils.py
import sys
import os

# Añadir la carpeta src al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import saludo, suma, resta

def test_saludo():
    assert saludo("Ana") == "Hola, Ana!"

def test_suma():
    assert suma(2,3) == 5

def test_resta():
    assert resta(5,2) == 3

if __name__ == "__main__":
    test_saludo()
    test_suma()
    test_resta()
    print("Todos los tests pasaron ✅")
