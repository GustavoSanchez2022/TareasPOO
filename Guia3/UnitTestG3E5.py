import unittest
from G3Ejercicio5 import Rectangulo

class MyTestCase(unittest.TestCase):
    def test_area(self):
        figura = Rectangulo(7,4)
        self.assertEqual(figura.area_rectangulo(), 28)

    def test_perimetro(self):
        figura = Rectangulo(5,4)
        self.assertEqual(figura.perimetro_rectangulo(), 18)

if __name__ == '__main__':
    unittest.main()
