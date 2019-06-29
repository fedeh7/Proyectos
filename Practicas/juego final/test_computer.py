import unittest
from computer import Computer

class TestComputer(unittest.TestCase):
    def test_inicio_computadora(self):
        juego = Computer()
        self.assertEqual(juego.guess, 0)
        self.assertEqual(juego.bien, 0)
        self.assertEqual(juego.regular, 0)
        self.assertTrue(juego.is_playing)
        self.assertFalse(juego.error)
        self.assertFalse(juego.loop_bien)
        self.assertFalse(juego.loop_regular)
        self.assertFalse(juego.loop_general)


    def test_play_ok(self):
        juego = Computer()
        self.assertTrue(juego.play())
        self.assertFalse(juego.error)
        self.assertTrue(juego.loop_bien)
        self.assertTrue(juego.loop_regular)
        self.assertTrue(juego.loop_general)

    def test_play_error(self):
        juego = Computer()
        juego.posibles = []
        self.assertFalse(juego.play())
        self.assertTrue(juego.error)

    def test_verificador_ok_bien(self):
        juego = Computer()
        juego.verificador("0", 1)
        self.assertFalse(juego.loop_bien)
        juego.verificador("1", 1)
        self.assertFalse(juego.loop_bien)
        juego.verificador("2", 1)
        self.assertFalse(juego.loop_bien)
        juego.verificador("3", 1)
        self.assertFalse(juego.loop_bien)
        juego.verificador("4", 1)
        self.assertFalse(juego.loop_bien)

    def test_verificador_ok_regular(self):
        juego = Computer()
        juego.verificador("0", 2)
        self.assertFalse(juego.loop_regular)
        juego.verificador("1", 2)
        self.assertFalse(juego.loop_regular)
        juego.verificador("2", 2)
        self.assertFalse(juego.loop_regular)
        juego.verificador("3", 2)
        self.assertFalse(juego.loop_regular)
        juego.verificador("4", 2)
        self.assertFalse(juego.loop_regular)

    def test_verificador_error(self):
        juego = Computer()
        self.assertFalse(juego.verificador("", 1))
        self.assertFalse(juego.verificador("11", 1))
        self.assertFalse(juego.verificador("5", 1))
        self.assertFalse(juego.verificador("A", 1))
        self.assertFalse(juego.verificador("", 2))
        self.assertFalse(juego.verificador("11", 2))
        self.assertFalse(juego.verificador("5", 2))
        self.assertFalse(juego.verificador("A", 2))
        self.assertFalse(juego.verificador("1", 3))
        self.assertFalse(juego.is_playing)
    def test_check_bienregular(self):
        juego = Computer()
        juego.bien = 3
        juego.regular = 3
        self.assertFalse(juego.check_bienregular())
        juego.bien = 3
        juego.regular = 1
        self.assertFalse(juego.check_bienregular())
        juego.bien = 1
        juego.regular = 1
        self.assertTrue(juego.check_bienregular())
        self.assertFalse(juego.loop_general)
        juego.bien = 2
        juego.regular = 2
        self.assertTrue(juego.check_bienregular())
        self.assertFalse(juego.loop_general)
        juego.bien = 4
        juego.regular = 0
        self.assertTrue(juego.check_bienregular())
        self.assertFalse(juego.loop_general)
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