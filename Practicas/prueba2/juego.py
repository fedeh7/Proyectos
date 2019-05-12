from computerclass import Computer
def main():
    num = input("\nElijamos un num")
    juego = Computer()
    while juego.is_playing == True:
        print(num)
        juego.play()
main()