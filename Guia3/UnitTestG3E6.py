import unittest
from G3Ejercicio6 import Punto

class MyTestCase(unittest.TestCase):
    def test_cuadrante(self):
        puntoEjemplo = Punto(2,4)
        self.assertEqual(puntoEjemplo.cuadrante(2,4), 1)  # add assertion here

    def test_pitagoras(self):
        puntoEjemplo = Punto(2,4)
        self.assertEqual(puntoEjemplo.pitagoras(), 4.47)

if __name__ == '__main__':
    unittest.main()
