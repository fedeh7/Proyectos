class RespuestaMuyChica(Exception):
    pass
class RespuestaMuyGrande(Exception):
    pass
class RespuestaConNumerosRepetidos(Exception):
    pass
    
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
    intentos = 0
    while x == 0:
        vector = []
        bien = 0
        regular = 0
        solucion = []
        respuesta = str(respuesta)
        for i in respuesta:
            solucion.append(int(i))
        #print("La solucion es: ",solucion)
        y = 0
        while y == 0:
            intentos = intentos + 1
            num = input("Ingrese un numero de 4 cifras distintas: ")
            vector = []
            if num.isnumeric() == True:
                for i in num:
                    vector.append(int(i))
                if len(num) != 4:
                    print("Error.Noson4numeros\nRecuerde que tienen que ser 4 numeros!")
                elif vector[0] == vector[1] or vector[0] == vector[2] or vector[0] == vector[3] or vector[1] == vector[2] or vector[1] == vector[3] or vector[2] == vector[3]:
                    print("Error.Haynumerosiguales\nRecuerde que los numeros tienen que ser distintos!")                     
                else:
                    #print("El numero ingresado es valido")
                    y = 1
            else: 
                print("Error.Hayletras\nTiene que ingresar solo 4 numeros! Diferentes!")
            
                
        #print(vector)

        for i in range(4):
            for j in range(4):
                if vector[j] == solucion[i] and i == j:
                    bien = bien + 1
                elif vector[j] == solucion[i] and i != j:
                    regular = regular + 1

        print("bien ", bien)
        print("regular ", regular)
        if bien == 4:
            for i in range(4):
                vector[i] = str(vector[i])
            r = int("".join(vector))
            print(f"Muy bien has ganado en {intentos} intentos!\nLa respuesta era {r}")
            x = 1
            return r
            