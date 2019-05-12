import unittest
from advmaquina import advmaquina

class Testmaquina(unittest.TestCase):
    
    def test_maquina_Letras(self):
        resultado = advmaquina("hola")
        self.assertEqual(resultado,"ValueError")
    def test_maquina_Repetidos(self):
        resultado = advmaquina(1581)
        self.assertEqual(resultado,"Repetidos")
    def test_maquina_Corta(self):
        resultado = advmaquina(123)
        self.assertEqual(resultado,"Muy Corta")
    def test_maquina_Larga(self):
        resultado = advmaquina(12345)
        self.assertEqual(resultado,"Muy Larga")
    def test_maquina_Valido(self):
        resultado = advmaquina(1234)
        self.assertEqual(resultado,1234)
        

if __name__ =='__main__':
    unittest.main()