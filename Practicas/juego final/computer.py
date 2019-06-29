import random

class Computer():  # Crea al jugador computadora
    def __init__(self):
        self.is_playing = True
        self.error = False
        self.guess = 0
        self.posibles = []
        self.generador()
        self.bien = 0
        self.regular = 0
        self.loop_bien = False
        self.loop_regular = False
        self.loop_general = False

###############################################################################
###############################################################################

    def check(self): # Compara el num que acaba de mandar, con todos los demas
        bien = 0                              # numeros posibles, y reduce la lista de posibles segun 
        regular = 0                              # los valores de "bien" y de "regular"
        not_posible = []
        self.posibles.remove(self.guess)
        for k in self.posibles:
            bien = 0
            regular = 0
            for i in range(4):
                for j in range(4):
                    if self.guess[j] == k[i] and i == j:
                        bien = bien + 1
                    elif self.guess[j] == k[i] and i != j:
                        regular = regular + 1
            if self.bien != bien or self.regular != regular:
                not_posible.append(k)
                #print("Agregando valor a not_posible")
        for borrar in not_posible:
            if borrar in self.posibles:
              #print("Borrando valor de posibles")
              self.posibles.remove(borrar)

###############################################################################
###############################################################################

    def play(self): # Intenta adivinar el num, sacandolo de la lista de numeros posibles
        
        try:
            self.guess = random.choice(self.posibles)
            print(f"Es el num {self.guess}?\n")
            self.loop_bien = True
            self.loop_regular = True
            self.loop_general = True
            return True
        except:
            print("A cometido un error en algun momento, y no quedan numeros posibles para seguir intentando")
            self.error = True
            return False
        

        
###############################################################################
###############################################################################

    def verificador(self,num,bien_o_regular): # Verifica que el usuario haya ingresado un numero valido para "bien" y "regular"
        valor = num
        if valor.isnumeric():
            valor = int(valor)
            if len(str(valor)) > 1 or len(str(valor)) < 1:
                print("Recuerde que tiene que ingresar un numero entre 0 y 4")
                return False
            elif valor > 4:
                print("El num no puede ser mayor que 4")
                return False
            else:
                # Numero ingresado es valido
                if bien_o_regular == 1:
                    self.bien = int(num)
                    self.loop_bien = False
                elif bien_o_regular == 2:
                    self.regular = int(num)
                    self.loop_regular = False
                else:
                    print("Hubo un error al identificar si el valor es de 'Bien' o de 'Regular'")
                    self.is_playing = False
                    return False
        else:
            print("No ingrese letras, ingrese un numero entre 0 y 4")
            return False

###############################################################################
###############################################################################

    def check_bienregular(self):  # Verifica que ambos valores combinados de 'bien' y 'regular' sean coherentes
        if self.bien + self.regular > 4 or (self.bien == 3 and self.regular == 1):
                print("\nA cometido un error al ingresar los 'bien' y 'regular', intente denuevo\n")    
                return False

        elif self.bien == 4 and self.regular == 0:
            print("Gane!")
            self.is_playing = False 
            self.loop_general = False
            return True

        else:
            self.loop_general = False
            return True






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