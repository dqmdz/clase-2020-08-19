import unittest
from main import suma


class Testing(unittest.TestCase):
    def test_suma(self):
        result = suma(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
