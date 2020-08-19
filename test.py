import unittest
from main import Persona


class Testing(unittest.TestCase):
    def test_valida_atributo(self):
        persona = Persona('Sandro')
        self.assertEqual(persona.__dict__, {'_Persona__nombre': 'Sandro'})


if __name__ == '__main__':
    unittest.main()
