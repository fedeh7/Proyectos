import unittest
from computerclass import Computer

class TestUsuario(unittest.TestCase):
    
    def Setup(self):
        self.game = Computer()

    def check(self, guess, solution):
        b = 0
        r = 0
        for i in range(4):
            for j in range(4):
                if guess[j] == solution[i] and i == j:
                    b = b + 1
                elif guess[j] == solution[i] and i != j:
                    r = r + 1
    
    def test_Computerclass(self):
        resultado = self.game.play()
        self.assertEqual(resultado,"ValueError")
    
if __name__ =='__main__':
    unittest.main()