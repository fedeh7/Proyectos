import random
from advusuario import advusuario
from advmaquina import advmaquina
def main():
    x = 0
    opcion = ""
    while x == 0:
        opcion = ""
        opcion = input("\nSi quiere adivinar el numero de la maquina ingrese 1, si quiere que la maquina adivine su numero ingrese 2: ")
        if opcion != "1" and opcion != "2":
            print("Debe ingresar '1' o '2'!")
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
            solucion = input("Ingrese el numero que quiere que la maquina adivine: ")
            advmaquina(solucion)
            x = 2
        else:
            print("Surgio un error en la eleccion de opciones")

main()