def advmaquina(solucion):
    x = 0
    bien = 0
    regular = 0
    intentos = 0
    intento = []
    respuesta = []
    for i in solucion:
        respuesta.append(int(i))
    while x == 0:
        respuesta = []
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
        respuesta.append(str(a))
        respuesta.append(str(b))
        respuesta.append(str(c))
        respuesta.append(str(d))
