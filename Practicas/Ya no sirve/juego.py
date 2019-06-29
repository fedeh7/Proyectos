import random
from advusuario import advusuario
from computerclass import Computer

def main():
    y = 0
    x = 0
    opcion = ""
    while x == 0:
        opcion = ""
        opcion = input("\nSi quiere adivinar el numero de la maquina ingrese 1, si quiere que la maquina adivine su numero ingrese 2: ")
        if opcion != "1" and opcion != "2":
            print("\nDebe ingresar '1' o '2'!")
        elif opcion == "1":
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
            #print(valores)
            solucion = "".join(valores)
            #print(solucion)
            advusuario(solucion)
            x = 1
        elif opcion == "2":
            num = input("\nElija un numero: ")
            juego = Computer()
            intento = 0
            while juego.is_playing == True:
                intento = intento + 1
                print("Recuerde que su numero es: ",num)
                juego.play()
            print(f"Termino en {intento} intentos")
            x = 1
        else:
            print("\nSurgio un error en la eleccion de opciones")

main()