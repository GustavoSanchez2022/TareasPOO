import unittest
from Ejer1parte6 import calcularDicimal

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calcularDicimal([1,1,1,1,1,1,1,1]),255)  # add assertion here
    def test_something2(self):
        self.assertEqual(calcularDicimal([0,0,0,0,0,0,0,0]),0)
    def test_something3(self):
        self.assertEqual(calcularDicimal([1,0,1,1,1,1,0,0]),188)


if __name__ == '__main__':
    unittest.main()
