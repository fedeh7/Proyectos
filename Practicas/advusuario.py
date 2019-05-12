class RespuestaMuyChica(Exception):
    pass
class RespuestaMuyGrande(Exception):
    pass
class RespuestaConNumerosRepetidos(Exception):
    pass
class BR_NoesLista(Exception):
    pass
class BR_VectorLenInvalida(Exception):
    pass
class BR_VectorConLetras(Exception):
    pass
class BR_VectorRepetidos(Exception):
    pass
class BR_VectorValoresDobles(Exception):
    pass
class BR_RespuestaConLetras(Exception):
    pass
class BR_RespuestaLenInvalida(Exception):
    pass
class BR_RespuestaRepetidos(Exception):
    pass

###################################################################################
###################################################################################
            # Esta funcion se asegura que la respuesta generada sea valida
            # y luego inicia el juego

def advusuario(respuesta):
    
    try:
        x = int(respuesta)
        z = str(respuesta)
        if len(z) < 4:
            raise RespuestaMuyChica("Muy Chica")
        elif len(z) > 4:
            raise RespuestaMuyGrande("Muy Grande")
        elif z[0] == z[1] or z[0] == z[2] or z[0] == z[3] or z[1] == z[2] or z[1] == z[3] or z[2] == z[3]:
            raise RespuestaConNumerosRepetidos("Repetidos")
        else:
            ingresodedato(respuesta)
            return respuesta
            
        
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


###################################################################################
###################################################################################
            # Esta funcion es la que controla el juego
            
def ingresodedato(solucion):
    intentos = 0
    win = 0
    x = 0
    while win == 0:
        intentos = intentos + 1
        print("solucion: ", solucion)
        #print("intentos: ", intentos)
        x = 0
        vector = []
        while x == 0:
            num = input("Ingrese un numero de 4 cifras distintas: ")
            vector = []
            vector = verificaciondedato(num)
            if vector != "invalido, hay letras" and vector != "invalido, hay repetidos" and vector != "invalido, cantidad incorrecta":
                x = 1
        pistas = bienregular(vector, solucion)
        if not isinstance(pistas, list):
            return "Error"
            break
        else: 
            print("Bien: ", pistas[0])
            print("Regular: ", pistas[1])
            if pistas[0] == 4:
                for i in range(4):
                    vector[i] = str(vector[i])
                r = "".join(vector)
                print(f"Muy bien has ganado en {intentos} intentos!\nLa respuesta era {r}")
                win = 1
    return solucion

###################################################################################
###################################################################################
            # Esta funcion verifica que el dato sea correcto

def verificaciondedato(num):
    if check_letras(num) == False:
        print("Error.Hayletras\nTiene que ingresar solo 4 numeros! Diferentes!")
        return "invalido, hay letras"
    elif check_len(num) == False:
        print("Error.Noson4numeros\nRecuerde que tienen que ser 4 numeros!")
        return "invalido, cantidad incorrecta"
    elif check_repetidos(num) == False:
        print("Error.Haynumerosiguales\nRecuerde que los numeros tienen que ser distintos!")                     
        return "invalido, hay repetidos"
    else:
        vector = []
        num = str(num)
        for i in num:
            vector.append(int(i))
        return vector
    
###################################################################################
###################################################################################
            # Esta funcion calcula los "bien" y los "regular"

def bienregular(vector, respuesta):
    if check_vector(vector) != True:
        return check_vector(vector)
    elif check_respuesta(respuesta) != True:
        return check_respuesta(respuesta)
    else:    
        bien = 0
        regular = 0
        solucion = []
        for i in str(respuesta):
            solucion.append(int(i))
        pistas = []
        for i in range(4):
            for j in range(4):
                if vector[j] == solucion[i] and i == j:
                    bien = bien + 1
                elif vector[j] == solucion[i] and i != j:
                    regular = regular + 1
        pistas.append(bien)
        pistas.append(regular)
        return pistas
    
###################################################################################
###################################################################################
            # Estas funciones checkean para encontrar distintas fallas posibles

def check_len(num):
    if isinstance(num, str):
        if len(str(num)) != 4:
            return False
        else:
            return True
    elif isinstance(num, list):
        if len(num) != 4:
            return False
        else:
            return True
    elif isinstance(num, int):
        if len(str(num)) != 4:
            return False
        else:
            return True

def check_letras(num):
    if isinstance(num, list):
        for i in num:
            if str(i).isnumeric() == False:
                return False
        return True
    elif isinstance(num, str):
        for i in num:
            if i.isnumeric() == False:
                return False
        return True
    elif isinstance(num, int):
        return True
    else:
        print("El valor es de una instancia invalida")
        return False

def check_repetidos(num):
    if isinstance(num, list):
        if str(num[0]) == str(num[1]) or str(num[0]) == str(num[2]) or str(num[0]) == str(num[3]) or str(num[1]) == str(num[2]) or str(num[1]) == str(num[3]) or str(num[2]) == str(num[3]):
            return False
        else:
            return True
    elif isinstance(num, str):
        if str(num[0]) == str(num[1]) or str(num[0]) == str(num[2]) or str(num[0]) == str(num[3]) or str(num[1]) == str(num[2]) or str(num[1]) == str(num[3]) or str(num[2]) == str(num[3]):
            return False
        else:
            return True
    elif isinstance(num, int):
        num = str(num)
        if str(num[0]) == str(num[1]) or str(num[0]) == str(num[2]) or str(num[0]) == str(num[3]) or str(num[1]) == str(num[2]) or str(num[1]) == str(num[3]) or str(num[2]) == str(num[3]):
            return False
        else:
            return True
    else:
        print("El valor es de una instancia invalida")
        return False

def check_valores_lista(num):
    if not isinstance(num, list):
        print("El Valor no es una lista")
        return False
    else: 
        for i in num:
            if len(str(i)) > 1:
                return False
        return True

###################################################################################
###################################################################################
            # Estas funciones checkean el vector y la respuesta en BienRegular
            # Las hice fuera de BienRegular por que sino me quedaba muy largo

def check_vector(vector):
    try:
        if not isinstance(vector, list):
            raise BR_NoesLista()
        elif check_len(vector) == False:
            raise BR_VectorLenInvalida
        elif check_letras(vector) == False:
            raise BR_VectorConLetras
        elif check_repetidos(vector) == False:
            raise BR_VectorRepetidos
        elif check_valores_lista(vector) == False:
            raise BR_VectorValoresDobles
        else:
            return True

    except BR_NoesLista:
        print("\nEl vector no es lista!")
        return "No es lista"
    except BR_VectorLenInvalida:
        print("\nEl vector no es de 4 digitos!")
        return "Vector Longitud Invalida"
    except BR_VectorConLetras:
        print("\nEl vector contiene letras!")
        return "Vector con letras"
    except BR_VectorRepetidos:
        print("\nEl vector tiene numeros repetidos!")
        return "Vector con numeros repetidos"
    except BR_VectorValoresDobles:
        print("\nEl vector tiene valores dobles!")
        return "Vector con valores dobles"

def check_respuesta(respuesta):
        
    try:    
        if check_letras(respuesta) == False:
            raise BR_RespuestaConLetras
        elif check_len(respuesta) == False:
            raise BR_RespuestaLenInvalida
        elif check_repetidos(respuesta) == False:
            raise BR_RespuestaRepetidos
        else:
            return True

    except BR_RespuestaConLetras:
        print("\nLa respuesta contiene letras!")
        return "Respuesta con letras"
    except BR_RespuestaLenInvalida:
        print("\nLa respuesta no es de 4 digitos!")
        return "Respuesta no es de 4 digitos"
    except BR_RespuestaRepetidos:
        print("\nLa respuesta tiene numeros repetidos!")
        return "Respuesta con numeros repetidos"
