import unittest
from G3Ejercicio1 import Calculadora

calculadora_nueva = Calculadora("Casio", "NULL", 1000000, "fx550")

class Test_G3Ejercicio1(unittest.TestCase):
    def test_something1(self):
        self.assertEqual(calculadora_nueva.sumar(200,5), 205)  # add assertion here
    def test_something2(self):
        self.assertEqual(calculadora_nueva.restar(200,5), 195)
    def test_something3(self):
        self.assertEqual(calculadora_nueva.multiplicacion(200,5), 1000)
    def test_something4(self):
        self.assertEqual(calculadora_nueva.division(20,5), 4)
    def test_something5(self):
        self.assertEqual(calculadora_nueva.factorial(5),120)


if __name__ == '__main__':
    unittest.main()
