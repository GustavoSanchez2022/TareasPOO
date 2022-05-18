import unittest
from G3Ejercicio2 import Lampara

class TestEjercicio2(unittest.TestCase):
    def test_something(self):
        lampara_nueva = Lampara()
        lampara_nueva.cambiar_estado()
        self.assertEqual(lampara_nueva.estado, True)  # add assertion here

    def test_something2(self):
        lampara_nueva2 = Lampara()
        lampara_nueva2.cambiar_estado()
        self.assertEqual(lampara_nueva2.cambiar_estado(), False)

if __name__ == '__main__':
    unittest.main()
