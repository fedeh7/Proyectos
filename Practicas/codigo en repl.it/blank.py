def blank(guess, matriz):
    matriz_blank = matriz[0]
    
    for i in range(0, 4):
        matriz_blank.remove(guess[i])
    
    for i in range(0, 4):
        matriz[i] = matriz_blank

    return matriz
    
    