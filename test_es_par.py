import unittest
from math_utils import es_par  # aún no existe -> queremos ver fallar RED

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))  # 4 debería ser par

if __name__ == "__main__":
    unittest.main()