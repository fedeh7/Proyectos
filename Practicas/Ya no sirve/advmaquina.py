import random

class RespuestaMuyChica(Exception):
    pass
class RespuestaMuyGrande(Exception):
    pass
class RespuestaConNumerosRepetidos(Exception):
    pass

def advmaquina(solucion):
    try:
        x = int(solucion)
        z = str(solucion)
        if len(z) < 4:
            raise RespuestaMuyChica("Muy Chica")
        elif len(z) > 4:
            raise RespuestaMuyGrande("Muy Grande")
        elif z[0] == z[1] or z[0] == z[2] or z[0] == z[3] or z[1] == z[2] or z[1] == z[3] or z[2] == z[3]:
            raise RespuestaConNumerosRepetidos("Repetidos")
        
    except ValueError:
        print("La respuesta contiene letras")
        return "ValueError"
    except RespuestaMuyChica:
        print("La respuesta es muy corta")
        return "Muy Corta"
    except RespuestaMuyGrande:
        print("La respuesta es muy Larga")
        return "Muy Larga"
    except RespuestaConNumerosRepetidos:
        print("La respuesta tiene numeros repetidos")
        return "Repetidos"


    x = 0
    y = 0
    bien = 0
    intentos = 0
    intento = []
    respuesta = []
    solucion = str(solucion)
    for i in solucion:
        respuesta.append(int(i))
    while x == 0:
        bien = 0
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
        for i in range(4):
            y = 0

            while y == 0:
                if respuesta[i] == intento[i]:
                    bien = bien + 1
                    y = 1
                else:
                    intento[i] = intento[i] + 1
                    intentos = intentos + 1
                    if intento[i] > 9:
                        intento[i] = 0

        if bien == 4:
            for i in range(4):
                intento[i] = str(intento[i])
            r = int("".join(intento))
            if intentos == 0:
                intentos = 1
            print("La respuesta era", r)
            print(f"resuelto en {intentos} intentos")
            x = 1
            return r
