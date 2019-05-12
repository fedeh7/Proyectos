import unittest
from advusuario import advusuario, ingresodedato, verificaciondedato, bienregular

class TestUsuario(unittest.TestCase):
    
    # Tests de la Respuesta
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
    """
    def test_usuario_Valido(self):  # Ingrese 1234 para probar que es correcto
        resultado = advusuario(1234)
        self.assertEqual(resultado,1234)
"""

    # Tests del verificador de dato
    def test_verificador_valido_str(self):
        resultado = verificaciondedato("1234")
        self.assertEqual(resultado,[1, 2, 3, 4])
    def test_verificador_valido_int(self):
        resultado = verificaciondedato(1234)
        self.assertEqual(resultado,[1, 2, 3, 4])
    def test_verificador_cantidad_incorrecta(self):
        resultado = verificaciondedato("12345")
        self.assertEqual(resultado,"invalido, cantidad incorrecta")
    def test_verificador_letras(self):
        resultado = verificaciondedato("hola")
        self.assertEqual(resultado,"invalido, hay letras")
    def test_verificador_repetidos(self):
        resultado = verificaciondedato("1134")
        self.assertEqual(resultado,"invalido, hay repetidos")
    
    # Test BienRegular validos
    def test_bienregular_correcto1(self):
        resultado = bienregular([1, 2, 3, 4], 1234)
        self.assertEqual(resultado, [4, 0])
    def test_bienregular_correcto2(self):
        resultado = bienregular([4, 3, 2, 1], 1234)
        self.assertEqual(resultado, [0, 4])
    def test_bienregular_correcto3(self):
        resultado = bienregular([2, 1, 3, 4], 1234)
        self.assertEqual(resultado, [2, 2])
    def test_bienregular_correcto4(self):
        resultado = bienregular([5, 6, 7, 8], 1234)
        self.assertEqual(resultado, [0, 0])

    # Test BienRegular de vector invalido
    def test_bienregular_invalido_VNoesLista(self):
        resultado = bienregular(1234, 1234)
        self.assertEqual(resultado, "No es lista")
    def test_bienregular_invalido_VLargo(self):
        resultado = bienregular([1, 2, 3, 4, 5], 1234)
        self.assertEqual(resultado, "Vector Longitud Invalida")
    def test_bienregular_invalido_VCorto(self):
        resultado = bienregular([1, 2, 3], 1234)
        self.assertEqual(resultado, "Vector Longitud Invalida")
    def test_bienregular_invalido_VConLetras(self):
        resultado = bienregular([1, "h", 3, 4], 1234)
        self.assertEqual(resultado, "Vector con letras")
    def test_bienregular_invalido_VRepetidos(self):
        resultado = bienregular([1, 2, 3, 3], 1234)
        self.assertEqual(resultado, "Vector con numeros repetidos")
    def test_bienregular_invalido_VDobles(self):
        resultado = bienregular([1, 22, 3, 4], 1234)
        self.assertEqual(resultado, "Vector con valores dobles")
    
    # Test BienRegular de respuesta invalida
    def test_bienregular_invalido_RLetras(self):
        resultado = bienregular([1, 2, 3, 4], "h23a")
        self.assertEqual(resultado, "Respuesta con letras")
    def test_bienregular_invalido_RCorta(self):
        resultado = bienregular([1, 2, 3, 4], 123)
        self.assertEqual(resultado, "Respuesta no es de 4 digitos")
    def test_bienregular_invalido_RLarga(self):
        resultado = bienregular([1, 2, 3, 4], 12345)
        self.assertEqual(resultado, "Respuesta no es de 4 digitos")
    def test_bienregular_invalido_RRepetidos(self):
        resultado = bienregular([1, 2, 3, 4], 1233)
        self.assertEqual(resultado, "Respuesta con numeros repetidos")







if __name__ =='__main__':
    unittest.main()