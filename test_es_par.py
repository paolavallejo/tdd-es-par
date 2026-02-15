import unittest
from math_utils import es_par

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))

    def test_5_no_es_par(self):
        # RED: 5 no es par
        self.assertFalse(es_par(5))

    def test_0_es_par(self):
        # 0 es considerado par
        self.assertTrue(es_par(0))

    def test_negativos(self):
        # negativos funcionan igual
        self.assertTrue(es_par(-2))
        self.assertFalse(es_par(-3))

if __name__ == "__main__":
    unittest.main()