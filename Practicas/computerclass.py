import random

class Computer():  # Crea al jugador computadora
    def __init__(self):
        self.is_playing = True
        self.guess = 0
        self.posibles = []
        self.generador()

###############################################################################
###############################################################################

    def check(self, guess, bien, regular): # Compara el num que acaba de mandar, con todos los demas
        b = 0                              # numeros posibles, y reduce la lista de posibles segun 
        r = 0                              # los valores de "bien" y de "regular"
        not_posible = []
        self.posibles.remove(guess)
        for k in self.posibles:
            b = 0
            r = 0
            for i in range(4):
                for j in range(4):
                    if guess[j] == k[i] and i == j:
                        b = b + 1
                    elif guess[j] == k[i] and i != j:
                        r = r + 1
            if bien != b or regular != r:
                not_posible.append(k)
                #print("Agregando valor a not_posible")
        for borrar in not_posible:
            if borrar in self.posibles:
              #print("Borrando valor de posibles")
              self.posibles.remove(borrar)

###############################################################################
###############################################################################

    def play(self): # Intenta adivinar el num, sacandolo de la lista de numeros posibles
        bien = 0
        regular = 0
        guess = 0
        x = 0
        try:
            guess = random.choice(self.posibles)
        except:
            print("A cometido un error en algun momento, y no quedan numeros posibles para seguir intentando")
        print(f"Es el num {guess}?\n")
        while x == 0:
            print("Bien?: ")
            bien = self.verificador()
            print("\nRegular?: ")
            regular = self.verificador()
            if bien == 3 and regular == 1:
                print("\nNo pueden haber 3 numeros bien y 1 regular, a cometido un error, intente denuevo\n")    
                print(f"Es el num {guess}?\n")
            else:
                x = 1       
        if bien == 4:
            print("Gane!")
            self.is_playing = False    
        else:
            self.check(guess, bien, regular)

###############################################################################
###############################################################################

    def verificador(self): # Verifica que el usuario haya ingresado un numero valido para "bien" y "regular"
        x = 0
        valor = 0
        while x == 0:
            valor = input()
            if valor.isnumeric():
                valor = int(valor)
                if len(str(valor)) > 1 or len(str(valor)) < 1:
                    print("Recuerde que tiene que ingresar un numero entre 0 y 4")
                elif valor > 4:
                    print("El num no puede ser mayor que 4")
                else:
                    # Numero ingresado es valido
                    return valor
                    x = 1
            else:
                print("No ingrese letras, ingrese un numero entre 0 y 4")

###############################################################################
###############################################################################

    def generador(self):    # Genera una lista de numeros validos para jugar
        num = [0, 0, 0, 0]
        for i in range(0, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    for p in range(0, 10):
                        num = [0, 0, 0, 0]
                        num[0] = i
                        num[1] = j
                        num[2] = k
                        num[3] = p
                        if num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
                            # no hago nada en este caso
                            #print("nope")
                            pass
                        else:
                            # El numero es valido y lo agrego a la lista de
                            # numeros posibles para jugar
                            self.posibles.append(num)
        #print(self.posibles)