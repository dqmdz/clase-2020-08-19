import unittest
from main import suma
from parameterized import parameterized


class Testing(unittest.TestCase):
    @parameterized.expand([[2, 3, 5], [3, 4, 7]])
    def test_suma(self, a, b, c):
        result = suma(a, b)
        self.assertEqual(result, c)


if __name__ == '__main__':
    unittest.main()
