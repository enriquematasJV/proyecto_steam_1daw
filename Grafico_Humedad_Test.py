import unittest
from vista import mostrar_grafico_humedad

class GraficoHumedadTest(unittest.TestCase):

    def setUp(self):
        self.mostrar_grafico_humedad = mostrar_grafico_humedad(self, humedades)

    def tearDown(self):
        self.mostrar_grafico_humedad = None

    def testGetMostrarGraficoHumedad(self):
        humedades = [10, 40, 50, 90]

        mostrar_grafico_humedad = self.mostrar_grafico_humedad(self, humedades)

        self.assertEqual(mostrar_grafico_humedad, self.mostrar_grafico_humedad)

if __name__ == '__main__':
    unittest.main()
