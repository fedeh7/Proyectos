from computerclass import Computer

def main():
  num = input("\nElija un numero: ")
  juego = Computer()
  intento = 0
  while juego.is_playing == True:
    intento = intento + 1
    print("Recuerde que su numero es: ",num)
    juego.play()
  print(f"Termino en {intento} intentos")
main()
