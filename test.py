import unittest

class TestGetValorMedio(unittest.TestCase):
    def setUp(self):
        self.objeto = get_valor_medio()  

    def test_get_valor_medio(self):
        # Caso de prueba 1: Lista vacía
        lista_vacia = []
        resultado_vacia = self.objeto.get_valor_medio(lista_vacia)
        self.assertEqual(resultado_vacia, 0)

        # Caso de prueba 2: Lista con elementos
        lista = [1, 2, 3, 4, 5]
        resultado = self.objeto.get_valor_medio(lista)
        # El valor medio de la lista [1, 2, 3, 4, 5] es 3
        self.assertEqual(resultado, 3)  
        

        # Caso de prueba 3: Lista con un solo elemento
        lista_un_elemento = [10]
        resultado_un_elemento = self.objeto.get_valor_medio(lista_un_elemento)
        self.assertEqual(resultado_un_elemento, 10) 
