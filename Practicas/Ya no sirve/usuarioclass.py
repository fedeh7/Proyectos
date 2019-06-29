import random

class Usuario():
    def __init__(self):
        self.respuesta = ""
        self.turno = 0
        self.bien = 0
        self.regular = 0
        self.is_playing = True
        self.generador()
    
    def generador(self):
        valores = []
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        while a == b:
            b = random.randint(0, 9)
        while c == b or c == a:
            c = random.randint(0, 9)
        while d == a or d == b or d == c:
            d = random.randint(0, 9)
        valores.append(str(a))
        valores.append(str(b))
        valores.append(str(c))
        valores.append(str(d))
        self.respuesta = "".join(valores)

    def check_bienregular(self, num):
        bien = 0
        regular = 0
        solucion = []
        intento = []
        for i in str(num):
            intento.append(int(i))
        for i in str(self.respuesta):
            solucion.append(int(i))
        for i in range(4):
            for j in range(4):
                if intento[j] == solucion[i] and i == j:
                    bien = bien + 1
                elif intento[j] == solucion[i] and i != j:
                    regular = regular + 1
        self.bien = bien
        self.regular = regular
        if self.bien == 4:
            self.is_playing = False

    def check_num(self, num):
        if len(str(num)) != 4:
            return False
        for i in num:
            if i.isnumeric() == False:
                return False
        if str(num[0]) == str(num[1]) or str(num[0]) == str(num[2]) or str(num[0]) == str(num[3]) or str(num[1]) == str(num[2]) or str(num[1]) == str(num[3]) or str(num[2]) == str(num[3]):
            return False
        
        return True
        
    def play(self, num):
        if self.check_num(num) == False:
            print("El numero ingresado es invalido, Intente denuevo")
        else:
            self.turno = self.turno + 1
            self.check_bienregular(num)
            print(f"Bien: {self.bien}")
            print(f"Regular: {self.regular}")

    

def main():
    intento = ""
    juego = Usuario()
    print(juego.respuesta)
    while juego.is_playing == True:
        intento = input("intento: ")
        juego.play(intento)
    print(f"Ganaste en {juego.turno} intentos")
main()