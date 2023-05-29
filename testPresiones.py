import unittest
from modelo import Mediciones

class MedicionesTest(unittest.TestCase):

    def setUp(self):
        self.medicion = Mediciones()

    def tearDown(self):
        self.medicion = None

    def testGetPresion(self):
        expected_presion = 1000.0
        self.medicion.sense.pressure = expected_presion

        presion = self.medicion.get_presion()

        self.assertEqual(presion, expected_presion)

    def testGetPresiones(self):
        expected_presiones = [1000.0, 1010.0, 990.0]
        self.medicion.sense.pressure = expected_presiones[-1]

        presiones = self.medicion.get_presiones()

        self.assertEqual(presiones, expected_presiones)

if __name__ == '__main__':
    unittest.main()
