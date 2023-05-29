import unittest
from unittest.mock import Mock
from modelo import Mediciones

# Creamos la clase prueba para no modificar la real, pero usa lo mismo, quitando sense_emu y sensehat
class Mediciones_Prueba:
    def __init__(self, sense):
        self.sense = sense
        self.temperaturas = []
        self.humedades = []

    def get_temperatura(self):
        t = round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t

    def get_temperaturas(self):
        return self.temperaturas

    def get_humedad(self):
        if self.sense.humidity is None:
            return None
        h = round(self.sense.humidity, 2)
        self.humedades.append(h)
        return h

    def get_humedades(self):
        return self.humedades

class MedicionTest(unittest.TestCase):
    def test_get_humedad(self):
        mock_sense = Mock()
        
        # Caso 1: Humedad menor a 0
        mock_sense.humidity = -1
        mediciones = Mediciones_Prueba(mock_sense)
        self.assertLess(mediciones.get_humedad(), 0)

        # Caso 2: Humedad mayor a 100
        mock_sense.humidity = 101
        mediciones = Mediciones_Prueba(mock_sense)
        self.assertGreater(mediciones.get_humedad(), 100)

        # Caso 3: Humedad vacía
        mock_sense.humidity = None
        mediciones = Mediciones_Prueba(mock_sense)
        self.assertIsNone(mediciones.get_humedad())

        # Caso 4: Humedad en rango válido
        mock_sense.humidity = 50
        mediciones = Mediciones_Prueba(mock_sense)
        self.assertGreaterEqual(mediciones.get_humedad(), 0)
        self.assertLessEqual(mediciones.get_humedad(), 100)

if __name__ == '__main__':
    unittest.main()
