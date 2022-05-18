import unittest
from G3Ejercicio7new import Segmento
from G3Ejercicio6 import Punto

class MyTestCase(unittest.TestCase):
    def test_lardo_del_segmento(self):
        segmente_a_b = Segmento(Punto(7,5),Punto(1,4))
        self.assertEqual(segmente_a_b.pitagoras(), 6.08)


if __name__ == '__main__':
    unittest.main()
