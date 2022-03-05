from unittest import result
from funciones import saludar
import unittest

class TestSaludar(unittest.TestCase):
    def test_success(self):
        resultado = saludar("Bryan")
        self.assertEqual(resultado, "Hola Bryan")

    def test_two(self):
        resultado = saludar("Juan")
        self.assertEqual(resultado, "Hola Juan")

if __name__ == '__main__':
    unittest.main()