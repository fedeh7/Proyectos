import random
from usuarioclass_final import Usuario
from computerclass_final import Computer

def main():
    loop_op = 0
    menu = 0
    opcion = ""
    while menu == 0:
        opcion = ""
        opcion = input("\nSi quiere adivinar el numero de la maquina ingrese 1, si quiere que la maquina adivine su numero ingrese 2: ")
        if opcion != "1" and opcion != "2":
            print("\nDebe ingresar '1' o '2'!")
        ########## Opcion 1 ##########        
        elif opcion == "1":
            intento = ""
            juego = Usuario()
            print(juego.respuesta)
            while juego.is_playing == True:
                intento = input("intento: ")
                juego.play(intento)
            print(f"Ganaste en {juego.turno} intentos")
        ########## Opcion 2 ##########    
        elif opcion == "2":
            num = input("\nElija un numero: ")
            juego = Computer()
            
            intento = 0
            while juego.is_playing == True:
                loop_op = 0
                bien = 0
                regular = 0
                loop_bien = 0
                loop_regular = 0
                intento = intento + 1
                print("Recuerde que su numero es: ",num)
                juego.play()
                if juego.error == True:
                    juego.is_playing = False
                    loop_op = 1
                while loop_op == 0:
                    while loop_bien == 0:
                        print("Bien?: ")
                        bien = input()
                        if juego.verificador(bien) == True:
                            bien = int(bien)
                            loop_bien = 1
                    while loop_regular == 0:        
                        print("\nRegular?: ")
                        regular = input()
                        if juego.verificador(regular) == True:
                            regular = int(regular)
                            loop_regular = 1
                    if juego.check_bienregular(bien, regular) == True:
                        juego.check()
                        loop_op = 1

            print(f"Termino en {intento} intentos")
            menu = 1
        else:
            print("\nSurgio un error en la eleccion de opciones")

main()