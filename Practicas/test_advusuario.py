import unittest
from advusuario import advusuario, ingresodedato, verificaciondedato, bienregular, victoria

class TestUsuario(unittest.TestCase):
    
    def test_usuario_Letras(self):
        resultado = advusuario("hola")
        self.assertEqual(resultado,"ValueError")
    def test_usuario_Repetidos(self):
        resultado = advusuario(1581)
        self.assertEqual(resultado,"Repetidos")
    def test_usuario_Corta(self):
        resultado = advusuario(123)
        self.assertEqual(resultado,"Muy Corta")
    def test_usuario_Larga(self):
        resultado = advusuario(12345)
        self.assertEqual(resultado,"Muy Larga")
    def test_usuario_Valido(self):
        resultado = advusuario(1234)
        self.assertEqual(resultado,1234)

    def test_dato_


if __name__ =='__main__':
    unittest.main()