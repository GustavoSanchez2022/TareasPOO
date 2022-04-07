import unittest
from Ejerecicio1b import colorPosicion


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(colorPosicion("a1"), "black")  # add assertion here
    def test_something2(self):
        self.assertEqual(colorPosicion("e5"), "black")
    def test_something3(self):
        self.assertEqual(colorPosicion("d1"), "white")
if __name__ == '__main__':
    unittest.main()
