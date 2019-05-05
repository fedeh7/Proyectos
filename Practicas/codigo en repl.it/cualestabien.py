def cual(guess, matriz, bien, regular):
    correctas = 0
    regulares = 0
    prueba = 0
    save_guess = guess
    save_matriz = matriz
    intentoa = matriz[0]
    intentob = matriz[1]
    intentoc = matriz[2]
    intentod = matriz[3]
    a = guess[0]
    b = guess[1]
    c = guess[2]
    d = guess[3]
    correctas = int(input("Bien?: "))
    regulares = int(input("Regulares?: "))
    if bien + regular == 4:
        del matriz[0]
        del matriz[1]
        del matriz[2]
        del matriz[3]
        matriz[0] = [a, b, c, d]
        matriz[1] = [a, b, c, d]
        matriz[2] = [a, b, c, d]
        matriz[3] = [a, b, c, d]
        guess[0] = b
        guess[1] = a
        print(guess)
        correctas = input("bien?: ")
        regulares = input("regulares?: ")
        if correctas == 4:
            print("Ganaste")
        elif correctas - bien == 2:
            matriz[0] = guess[0]
            matriz[1] = guess[1]
            guess[2] = d
            guess[3] = c
            print(guess)
            correctas = input("bien?: ")
            regulares = input("regulares?: ")
            if correctas == 4:
                print("Ganaste")
        elif correctas - bien == 1:
            guess[0] = a
            guess[1] = b

    elif bien + regular == 3:
            
