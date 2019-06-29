import unittest
from usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_inicio_usuario(self):
        juego = Usuario()
        self.assertTrue(juego.is_playing)
        self.assertEqual(juego.bien, 0)
        self.assertEqual(juego.turno, 0)
        self.assertEqual(juego.regular, 0)
    
    def test_bienregular_usuario(self):
        juego = Usuario()
        juego.respuesta = "1234"
        juego.check_bienregular("1243")
        self.assertEqual(juego.bien, 2)
        self.assertEqual(juego.regular, 2)
        self.assertTrue(juego.is_playing)

    def test_win(self):
        juego = Usuario()
        juego.respuesta = "1234"
        juego.play("1234")
        self.assertEqual(juego.bien, 4)
        self.assertEqual(juego.regular, 0)
        self.assertFalse(juego.is_playing)

    def test_checknum(self):
        juego = Usuario()
        prueba = juego.check_num("")
        self.assertFalse(prueba)
        prueba = juego.check_num("12345")
        self.assertFalse(prueba)
        prueba = juego.check_num("12EA")
        self.assertFalse(prueba)
        prueba = juego.check_num("1134")
        self.assertFalse(prueba)
        prueba = juego.check_num("1234")
        self.assertTrue(prueba)

    def test_simulation(self):
        juego = Usuario()
        juego.respuesta = "1234"
        juego.play("4567")
        self.assertEqual(juego.regular, 1)
        self.assertEqual(juego.bien, 0)
        self.assertTrue(juego.is_playing)
        juego.play("1267")
        self.assertEqual(juego.regular, 0)
        self.assertEqual(juego.bien, 2)
        self.assertTrue(juego.is_playing)
        juego.play("1234")
        self.assertEqual(juego.regular, 0)
        self.assertEqual(juego.bien, 4)
        self.assertFalse(juego.is_playing)







if __name__ =='__main__':
    unittest.main()