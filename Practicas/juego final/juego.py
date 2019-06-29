import random
from usuario import Usuario
from computer import Computer

def main():
    intento = 0
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
            #print(juego.respuesta)
            while juego.is_playing:
                intento = input("intento: ")
                juego.play(intento)
            print(f"Ganaste en {juego.turno} intentos")
            menu = 1
        ########## Opcion 2 ##########    
        elif opcion == "2":
            num = input("\nElija un numero: ")
            juego = Computer()
            while juego.is_playing:
                bien = regular = 0
                intento = intento + 1
                print("Recuerde que su numero es: ",num)
                juego.play()
                if juego.error:
                    juego.is_playing = False
                while juego.loop_general:
                    while juego.loop_bien:
                        bien = input("Bien?:\n")
                        juego.verificador(bien, 1)
                    while juego.loop_regular:        
                        regular = input("Regular?:\n")
                        juego.verificador(regular, 2)
                    if juego.check_bienregular():
                        juego.check()
            print(f"Termino en {intento} intentos")
            menu = 1


        # Error al elegir opción  
        else:
            print("\nSurgio un error en la eleccion de opciones")

main()