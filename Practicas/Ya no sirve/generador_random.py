def generador(posibilidades):
    
    intento = []
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
    intento.append(int(a))
    intento.append(int(b))
    intento.append(int(c))
    intento.append(int(d))
    return intento