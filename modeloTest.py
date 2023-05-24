import unittest
from modelo import Mediciones

class ModeloTest(unittest.TestCase):

    def setUp(self):
        self.medicion = Mediciones()

    def tearDown(self):
        self.medicion = None

    def testGet_Valor_Max(self):
        listaPrueba = [1,2,3,4,5]
        self.assertEqual(self.medicion.get_valor_max(listaPrueba),5,"El valor maximo debe ser 5")
        print("Se ha ejecutado testGet_Valor_Max")

    def testGet_Valor_Min(self):
        listaPrueba = [1,2,3,4,5]
        self.assertEqual(self.medicion.get_valor_min(listaPrueba),1,"El valor minimo debe ser 1")
        print("Se ha ejecutado testGet_Valor_Min")

if __name__ == '__main__':
    unittest.main()
