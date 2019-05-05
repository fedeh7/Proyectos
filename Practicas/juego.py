import random
from advusuario import advusuario
from advmaquina import advmaquina
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
            solucion = ""
            while y == 0:
                vector = []
                solucion = input("\nIngrese el numero que quiere que la maquina adivine: ")
                if solucion.isnumeric() == True:
                    for i in solucion:
                        vector.append(i)
                    if len(solucion) != 4:
                        print("\nError.Noson4numeros\nRecuerde que tienen que ser 4 numeros!")
                    elif vector[0] == vector[1] or vector[0] == vector[2] or vector[0] == vector[3] or vector[1] == vector[2] or vector[1] == vector[3] or vector[2] == vector[3]:
                        print("\nError.Haynumerosiguales\nRecuerde que los numeros tienen que ser distintos!")                     
                    else:
                        #print("El numero ingresado es valido")
                        y = 1
                else: 
                    print("\nError.Hayletras\nTiene que ingresar solo 4 numeros! Diferentes!")
            advmaquina(solucion)
            x = 2
        else:
            print("\nSurgio un error en la eleccion de opciones")

main()