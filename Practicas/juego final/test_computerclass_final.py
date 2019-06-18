import unittest
from computerclass_final import Computer

class TestUsuario(unittest.TestCase):
    def test_inicio_computadora(self):
        juego = Computer()
        self.assertEqual(juego.guess, 0)
        self.assertEqual(juego.bien, 0)
        self.assertEqual(juego.regular, 0)
        self.assertTrue(juego.is_playing)
        self.assertFalse(juego.error)
    
    def test_play_ok(self):
        juego = Computer()
        self.assertTrue(juego.play())
        self.assertFalse(juego.error)

    def test_play_error(self):
        juego = Computer()
        juego.posibles = []
        self.assertFalse(juego.play())
        self.assertTrue(juego.error)

    def test_verificador_ok(self):
        juego = Computer()
        self.assertTrue(juego.verificador("0"))
        self.assertTrue(juego.verificador("1"))
        self.assertTrue(juego.verificador("2"))
        self.assertTrue(juego.verificador("3"))
        self.assertTrue(juego.verificador("4"))

    def test_verificador_error(self):
        juego = Computer()
        self.assertFalse(juego.verificador(""))
        self.assertFalse(juego.verificador("11"))
        self.assertFalse(juego.verificador("5"))
        self.assertFalse(juego.verificador("A"))

    def test_check_bienregular(self):
        juego = Computer()
        self.assertFalse(juego.check_bienregular(3, 3))
        self.assertFalse(juego.check_bienregular(3, 1))
        self.assertTrue(juego.check_bienregular(1, 1))
        self.assertTrue(juego.check_bienregular(2, 2))
        self.assertTrue(juego.check_bienregular(4, 0))
        self.assertFalse(juego.is_playing)

    def test_check_1(self):  # Respuesta = [1, 2, 4, 3]
        juego = Computer()
        juego.guess = [1, 2, 3, 4]
        juego.bien = 2
        juego.regular = 2
        juego.check()
        self.assertEqual(juego.posibles.count([1, 2, 4, 3]), 1)
        self.assertEqual(juego.posibles.count([2, 1, 3, 4]), 1)
        self.assertEqual(juego.posibles.count([3, 2, 1, 4]), 1)
        self.assertEqual(juego.posibles.count([1, 3, 2, 4]), 1)
        self.assertEqual(juego.posibles.count([1, 2, 3, 4]), 0)

    def test_check_2(self):  # Respuesta = [1, 2, 4, 3]
        juego = Computer()
        juego.guess = [5, 6, 7, 8]
        juego.bien = 0
        juego.regular = 0
        juego.check()
        self.assertEqual(juego.posibles.count([5, 6, 7, 8]), 0)
        self.assertEqual(juego.posibles.count([1, 2, 3, 5]), 0)
        self.assertEqual(juego.posibles.count([0, 9, 2, 4]), 1)
        self.assertEqual(juego.posibles.count([1, 2, 4, 3]), 1)


if __name__ =='__main__':
    unittest.main()