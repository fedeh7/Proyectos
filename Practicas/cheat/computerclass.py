import random

class Computer():
    def __init__(self):
        self.is_playing = True
        self.guess = 0
        self.posibles = []
        self.generador()
    def check(self, guess, bien, regular):
        b = 0
        r = 0
        new_posible = []
        for k in range(0, len(self.posibles)):
            b = 0
            r = 0
            for i in range(4):
                for j in range(4):
                    if guess[j] == self.posibles[k][i] and i == j:
                        b = b + 1
                    elif guess[j] == self.posibles[k][i] and i != j:
                        regular = regular + 1
            if bien == b and regular == r:
                new_posible.append(self.posibles[k])
        self.posibles = new_posible

    def play(self):
        guess = random.choice(self.posibles)
        print(f"Es el num {guess}?")
        bien = int(input("Bien?: "))
        regular = int(input("Regular?: "))
        if bien == 4:
            print("Gane!")
            self.is_playing == False
        else:
            self.check(guess, bien, regular)
                    





    def generador(self):
        num = [0, 0, 0, 0]
        for i in range(0, 10):
            num[0] = i
            for j in range(0, 10):
                num[1] = j
                for k in range(0, 10):
                    num[2] = k
                    for p in range(0, 10):
                        num[3] = p
                        if num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
                            # no hago nada en este caso
                            print("nope")
                        else:
                            self.posibles.append(num)
        print(self.posibles)
