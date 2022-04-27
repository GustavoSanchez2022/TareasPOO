import unittest
from G1Ejercicio1 import Ejercicio

class TestEjercicio1(unittest.TestCase):
    def test_something1(self):
        self.assertEqual(Ejercicio(25,21,125), True)

    def test_something2(self):
        self.assertEqual(Ejercicio(55, 226, 5190), True)

    def test_something3(self):
        self.assertEqual(Ejercicio(12, 215, 2142), False)


if __name__ == '__main__':
    unittest.main()
