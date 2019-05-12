import random
from generador import generador
from blank import blank
from total4 import total4
#solucion = input("ingrese el num")
solucion = [1, 2, 3, 4]
matriz = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
save = 0
posibles = []
trys = 1
x = 0
while x == 0:
  print("intento: ",trys)
  bien = 0
  regular = 0
  save_bien = bien
  save_regular = regular
  matriz_a = matriz[0]
  matriz_b = matriz[1]
  matriz_c = matriz[2]
  matriz_d = matriz[3]
  guess = generador(matriz)
  print(guess)
  print(solucion)
  # Guardo los valores de bien y regular para comparar
  bien = int(input("Bien: "))
  save_bien = bien
  regular = int(input("Regular: "))
  save_regular = regular
  if bien == 4:
    print("Ganaste")
    x = 1
  elif bien + regular == 4:
    total4(guess, matriz, bien, regular)
  elif bien + regular == 0:
    matriz = blank(guess, matriz)
  elif bien > 0 or regular > 0:
    if len(str(matriz_d)) != 1:
      
      save = guess[3]
      guess[3] = random.choice(matriz_d)
      while save == guess[3] and guess[0] == guess[3] and guess[1] == guess[3] and guess[2] == guess[3]:
        guess[3] = random.choice(matriz_d)
      print(guess)
      # Pregunto si esta bien denuevo
      bien = int(input("bien?: "))
      regular = int(input("regular?: "))
      # Si antes tenia mas bien que ahora, es por q el anterior era un BIEN
      # y modifico la lista para dejar solo ese bien
      if save_bien > bien:
        guess[3] = save
        matriz_d = [save]
        matriz[3] = matriz_d
      # Si ahora tengo mas bien es por que el nuevo num es un BIEN
      # y modifico la lista para dejar solo ese bien
      elif bien > save_bien:
        matriz_d = [guess[3]]
        matriz = matriz_d
      if save_regular > regular and bien == save_bien:
        matriz_d.remove(guess[3])
        if matriz_a.count(guess[3]) > 0:
          matriz_a.remove(guess[3])
        if matriz_b.count(guess[3]) > 0:
          matriz_b.remove(guess[3])
        if matriz_c.count(guess[3]) > 0:
          matriz_c.remove(guess[3])
      elif regular > save_regular and bien == save_bien:
        matriz_d.remove(save)
        if matriz_a.count(save) > 0:
          matriz_a.remove(save)
        if matriz_b.count(save) > 0:
          matriz_b.remove(save)
        if matriz_c.count(save) > 0:
          matriz_c.remove(save)
      elif regular > save_regular and save_bien > bien
        posibles.append(guess[3])
        guess[3] = save
        matriz_d = [save]
        matriz[3] = matriz_d


  """for i in range(0, 4):
    if guess[i] == solucion[i]:
      del intento[i]
      intento.insert(i,guess[i])
    else:
      intento[i].remove(guess[i])"""
  trys = trys + 1
  """for i in range (0, 4):
    if guess[i] == solucion[i]:
      bien = bien + 1
      if bien == 4:
        x = 1
        print("intentos: ", trys)"""
    
