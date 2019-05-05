import random
def generador(intento):
  intentoa = intento[0]
  intentob = intento[1]
  intentoc = intento[2]
  intentod = intento[3]
  
  print(intentoa)
  print(intentob)
  print(intentoc)
  print(intentod)
  guess = []
  a = 0
  b = 0
  c = 0
  d = 0
  #lo que comente abajo creo q se puede borrar por q el while q sigue puede hacerlo todo solo
  """
  if len(str(intentoa)) == 1:
    a = intentoa
  else:
    a = random.choice(intentoa)

  if len(str(intentob)) == 1:
    b = intentob
  else:
    b = random.choice(intentob)

  if len(str(intentoc)) == 1:
    c = intentoc
  else:
    c = random.choice(intentoc)

  if len(str(intentod)) == 1:
    d = intentod
  else:
    d = random.choice(intentod)
    """

  while a == b or a == c or a == d or b == c or b == d or c == d:
      if len(str(intentoa)) == 1:
        a = intentoa
      else:
        a = random.choice(intentoa)
      
      if len(str(intentob)) == 1:
        b = intentob
      else:
        b = random.choice(intentob)
      
      if len(str(intentoc)) == 1:
        c = intentoc
      else:
        c = random.choice(intentoc)
      
      if len(str(intentod)) == 1:
        d = intentod
      else:
        d = random.choice(intentod)
      
  guess.append(int(a))
  guess.append(int(b))
  guess.append(int(c))
  guess.append(int(d))
  
  return guess