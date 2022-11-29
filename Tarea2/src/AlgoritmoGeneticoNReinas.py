#Algoritmo genetico para el problema de las n reinas.
#Integrantes:
# Casas Espinosa Axel
# Maldonado Vázquez Alejandro
# Martinez Enriquez Bruno
# Rivera Garcia Ignacio

import random
from numpy.random import randint
from numpy.random import rand

# las n reinas, un cromosoma se forma de la siguiente manera:
# 
#   Cada entrada i del arreglo corresponde a la columna donde esta una reina,
#   el numero en la entrada a[i] corresponde a la fila/renglon de la reina.
#
#     Por ejemplo, las coordenadas de las reinas para  [2,1,4,5,8,7,4,1]:
#     (2,1), (1,2), (4,3), (5,4), (8,5), (7,6), (4,7), (1,8)


# Funcion fitness nos regresa el valor fitness de un cromosoma x. El cual se calcula
# restando el maximo numero de conflictos para n reinas menos el numero de
# conflictos para el cromosoma x. Es decir, mientras mayor sea el fitness
# estara mejor optimizado (menos conflictos).
# n es la dimension del tablero para adaptarlo al problema de las n reinas.
def fitness(x,n):
  #maximo numero de conflictos para el problema de las n reinas.
  maxconflictos = n*(n-1)
  conflictos = 0

  #conflictos con filas.
  for i in range(len(x)):
    for j in range(len(x)):
      if i == j:
        continue
      if x[i] == x[j]:
        conflictos+=1

  #conflictos con diagonales ascendentes.
  for i in range(len(x)):
    for j in range(len(x)):
      if i == j:
        continue
      diagAi = i + x[i]
      diagAj = j + x[j]
      if diagAi == diagAj:
        conflictos+=1

  #conflictos con diagonales descendentes.
  for i in range(len(x)):
    for j in range(len(x)):
      if i == j:
        continue
      diagDi = i - x[i]
      diagDj = j - x[j]
      if diagDi == diagDj:
        conflictos+=1

  return maxconflictos - conflictos

# Inicializacion de cromosomas. Se generan un numero particular de cromosomas
# (numcrom) apartir de la dimension del tablero n.
def ini_pob(numcrom, n):
  cromo = list()
  for i in range(numcrom):
    #generacion de un cromosoma con n entradas (dimension del tablero)
    a = [0] * n
    for j in range(n):
      e = randint(1,n+1)
      a[j] = e
    cromo.append(a)
  return cromo

# Seleccion del algoritmo genetico basado en torneo. Se enfrenta a cada cromosoma
# con otro, en cada enfrentamiento el que tenga un mejor (mayor) fitness.
def selection(cromosomas, scores):
  nuevapob = list()
  #generacion de una lista de los cromosomas en orden aleatorio (sin repetir)
  enfrentamientos = random.sample(range(len(cromosomas)),len(cromosomas))
  for i in range(0,len(enfrentamientos),2):
    if scores[enfrentamientos[i]] > scores[enfrentamientos[i+1]]:
      nuevapob.append(cromosomas[enfrentamientos[i]])
    else:
      nuevapob.append(cromosomas[enfrentamientos[i+1]])
  #caso particular cuando la seleccion contiene un numero impar de cromosomas.
  if((len(nuevapob) % 2) == 1):
    a = randint(0, len(cromosomas))
    nuevapob.append(cromosomas[a])
  return nuevapob

# Crossover del algoritmo genetico donde dos padres generan nuevos hijos.
# El crossover solo ocurre cuando se cumple el ratio. Por defecto los hijos
# son copias identicas de los padres.
def crossover(padre1, padre2, r):
  hijo1 = padre1.copy()
  hijo2 = padre2.copy()

  if rand() < r:
    #punto de entrecruzamiento aleatorio.
    crosspoint = randint(1,len(padre1)-2)
    #nuevos hijos.
    hijo1 = padre1[:crosspoint] + padre2[crosspoint:]
    hijo2 = padre2[:crosspoint] + padre1[crosspoint:]
  return [hijo1, hijo2]

# Mutacion del algoritmo genetico donde cada entrada del cromosoma puede "mutar"
# con una probabilidad pequeña, generando un numero aleatorio correspondiente a
# un nuevo renglon.
def mutation(x, r, n):
  for i in range(len(x)):
    if rand() < r:
      x[i] = randint(1,n+1)

# tab_conflict funcion auxiliar para generar una lista de scores. Una lista de los fitness
# de los cromosomas que conforman la poblacion. 
def tab_conflict(pob,n):
  scores = list()
  for i in range(len(pob)):
    fit = fitness(pob[i],n)
    scores.append(fit)
  return scores

# algoritmo_genetico que ejecuta todos los pasos para resolver el problema de las
# n reinas.
#
# dim_tab corresponde a la dimension del tablero de ajedrez (las n reinas).
# n_iter corresponde al numero de iteraciones que se haran.
# n_pob corresponde al numero de cromosomas con los que empezara el algoritmo.
# r_cross corresponde al ratio de encruzamiento.
# r_mut corresponde al ratio de mutacion.
def algoritmo_genetico(dim_tab, n_iter, n_pob, r_cross, r_mut):
  #generacion de la poblacion inicial.
  poblacion = ini_pob(n_pob, dim_tab)
  #varialbe para el mejor cromosoma.
  best = 0
  #fitness del mejor cromosoma.
  best_eval = fitness(poblacion[0],dim_tab)
  #ciclo principal para las n_iteraciones
  for gen in range(n_iter):
    #lista de scores de la generacion.
    scores = tab_conflict(poblacion,dim_tab)

    #mejor cromosoma de la generacion.
    for i in range(len(poblacion)):
      if scores[i] > best_eval:
        best = poblacion[i]
        best_eval = scores[i]
    
    #seleccion natural.
    selected = selection(poblacion, scores)
    
    #generacion de la nueva generacion.
    children = list()
    for i in range(0, len(selected), 2):
      p1 = selected[i]
      p2 = selected[i+1]
      for c in crossover(p1,p2,r_cross):
        mutation(c,r_mut,dim_tab)
        children.append(c)
    #nueva gen
    poblacion = children
  return[best,best_eval]

#ejemplo con 8 reinas, 100 iteraciones, 500 cromosomas, 0.9 de crossover y 0.001 de mutacion.
algoritmo_genetico(8,100,500,0.9,0.001)