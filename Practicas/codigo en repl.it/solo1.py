def solo1(guess, matriz, bien, regular):
    seguros = [0, 0, 0, 0]
    for i in range(4):
        if len(matriz[i]) == 1:
            seguro[i] = 1
    save_guess = guess
    save_num = 0
    if seguros[0] == 0 and seguros[1] == 0:
        save_num = guess[0]
        guess[0] = guess[1]
        guess[1] = save_num
        print(guess)
        nuevas_bien = int(input("bien?: "))
        nuevas_regular = int(input("regulares?: "))
        if nuevas_bien > bien:
            save_num = guess[1]
            guess[1] = guess[2]
            guess[2] = save_num
            print(guess)
            nuevas_bien = int(input("bien?: "))
            nuevas_regular = int(input("regulares?: "))
            if nuevas_bien > bien:

