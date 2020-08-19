import unittest
from main import suma


class Testing(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
