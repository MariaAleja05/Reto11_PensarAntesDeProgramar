# Reto número 11 repo
### Fecha:  30-10-2023
* Mirar archivo Reto11.ipynb
  
**1.** Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
* EXPLICACIÓN
* Mirar archivo Punto_1.py
```pseudocode
def CrearMatriz(matriz_1, matriz_2):                                           # Para que el usuario cree la matriz

  print("Para la primera matriz: ")

  fila=[]
  filas=int(input("Ingrese el número de filas: "))                             # Ingresar el número de filas que quiere
  columnas=int(input("Ingrese el número de columnas: "))                       # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
  for i in range(filas):                                                       # Para ir creando cada fila
    for j in range(columnas):                                                  # Para añadir los valores de la fila (cada columna)
      valor=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila.append(valor)                                                       # Se añade el valor a la fila
    matriz_1.append(fila)                                                      # Se añade la fila terminada a la matriz
    fila=[]                                                                    # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")

  print("Para la segunda matriz: ")

  fila_2=[]
  filas_2=int(input("Ingrese el número de filas: "))                           # Ingresar el número de filas que quiere
  columnas_2=int(input("Ingrese el número de columnas: "))                     # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
  for i in range(filas_2):                                                     # Para ir creando cada fila
    for j in range(columnas_2):                                                # Para añadir los valores de la fila (cada columna)
      valor_2=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila_2.append(valor_2)                                                   # Se añade el valor a la fila
    matriz_2.append(fila_2)                                                    # Se añade la fila terminada a la matriz
    fila_2=[]                                                                  # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")
  print("Matriz #1")
  for k in range(len(matriz_1)):                                               # Para imprimir la primera matriz con forma de matriz ;)
    print(matriz_1[k])
  print("--------------------------------------------")
  print("Matriz #2")
  for k in range(len(matriz_2)):                                               # Para imprimir la segunda matriz con forma de matriz ;)
    print(matriz_2[k])

  if filas!=filas_2 and columnas!=columnas_2:                                  # Mirar si se pueden sumar o restar
    print("Las matrices no cumplen con las condiciones para realizar la operación")
  else:                                                                        # La opración que quiera hacer el usuario
    operacion=str(input("Ingrese 'sumar' si desea sumar las matrices o 'restar' si desea restar las matrices: "))
    if operacion=="sumar":                                                        # Para llamar la función suma
     Suma(matriz_1, matriz_2, resultado_matriz)
    elif operacion=="restar":                                                     # Para llamar la función suma
     Resta(matriz_1, matriz_2, resultado_matriz)

def Suma(matriz_1, matriz_2, resultado_matriz):                                # Se crea la función de la suma
  fila_sumada=[]                                                               # Para ir añadiendo las nuevas filas con los resultados sumados
  for i in range(len(matriz_1)):                                               # Para que vaya tomando cada fila
    fila_sumada = []                                                           # Para que no se acumulen los valores que se van sumando de las nuevas filas
    for j in range(len(matriz_1[0])):                                          # Para tomar la posición cada elemento
      suma = matriz_1[i][j] + matriz_2[i][j]                                   # Para tomar los números de las mismas coordenadas en cada matriz y sumarlas
      fila_sumada.append(suma)                                                 # Añadir la suma a la nueva fila de la matriz sumada
    resultado_matriz.append(fila_sumada)                                       # Añadir la fila terminada a la matriz resultante
  print("--------------------------------------------")
  print("Resultado de la suma de las matrices")
  for k in range(len(resultado_matriz)):                                       # Para imprimir la primera matriz con forma de matriz ;)
    print(resultado_matriz[k])

def Resta(matriz_1, matriz_2, resultadi_matriz):                               # Se crea la función de la resta
  fila_restada=[]                                                              # Para ir añadiendo las nuevas filas con los resultados restados
  for i in range(len(matriz_1)):                                               # Para que vaya tomando cada fila
    fila_restada = []                                                          # Para que no se acumulen los valores que se van restando de las nuevas filas
    for j in range(len(matriz_1[0])):                                          # Para tomar la posición cada elemento
      resta = matriz_1[i][j] - matriz_2[i][j]                                  # Para tomar los números de las mismas coordenadas en cada matriz y restarla
      fila_restada.append(resta)                                               # Añadir la resta a la nueva fila de la matriz restada
    resultado_matriz.append(fila_restada)                                      # Añadir la fila terminada a la matriz resultante

  print("--------------------------------------------")
  print("Resultado de la resta de las matrices")
  for k in range(len(resultado_matriz)):                                       # Para imprimir la primera matriz con forma de matriz ;)
    print(resultado_matriz[k])

if __name__ == "__main__":
  matriz_1=[]                                                                  # Se crea la matriz vacía
  matriz_2=[]                                                                  # Se crea la matriz vacía
  resultado_matriz=[]                                                          # El resultado de la operacion
  CrearMatriz(matriz_1, matriz_2)                                              # Se llama la función para crear la matriz1
```
**2.** Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
* EXPLICACIÓN
* Mirar archivo Punto_2.py
```pseudocode
def CrearMatriz(matriz_1, matriz_2):                                           # Para que el usuario cree la matriz

  print("Para la primera matriz: ")

  fila=[]
  filas=int(input("Ingrese el número de filas: "))                             # Ingresar el número de filas que quiere
  columnas=int(input("Ingrese el número de columnas: "))                       # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
  for i in range(filas):                                                       # Para ir creando cada fila
    for j in range(columnas):                                                  # Para añadir los valores de la fila (cada columna)
      valor=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila.append(valor)                                                       # Se añade el valor a la fila
    matriz_1.append(fila)                                                      # Se añade la fila terminada a la matriz
    fila=[]                                                                    # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")

  print("Para la segunda matriz: ")

  fila_2=[]
  filas_2=int(input("Ingrese el número de filas: "))                           # Ingresar el número de filas que quiere
  columnas_2=int(input("Ingrese el número de columnas: "))                     # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
  for i in range(filas_2):                                                     # Para ir creando cada fila
    for j in range(columnas_2):                                                # Para añadir los valores de la fila (cada columna)
      valor_2=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila_2.append(valor_2)                                                   # Se añade el valor a la fila
    matriz_2.append(fila_2)                                                    # Se añade la fila terminada a la matriz
    fila_2=[]                                                                  # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")
  print("Matriz #1")
  for k in range(len(matriz_1)):                                               # Para imprimir la primera matriz con forma de matriz ;)
    print(matriz_1[k])
  print("--------------------------------------------")
  print("Matriz #2")
  for k in range(len(matriz_2)):                                               # Para imprimir la segunda matriz con forma de matriz ;)
    print(matriz_2[k])

  if columnas!=filas_2:                                                        # Mirar si se puede realizar el producto
    print("Las matrices no cumplen con las condiciones para realizar la operación")
  else:
    Producto(matriz_1, matriz_2, matriz_producto)

def Producto(matriz_1, matriz_2, matriz_producto):
  for i in range(len(matriz_1)):
    fila = []
    for j in range(len(matriz_2[0])):
      fila.append(0)
    matriz_producto.append(fila)

  for i in range(len(matriz_1)):
    for j in range(len(matriz_2[0])):
      for k in range(len(matriz_1[0])):
        matriz_producto[i][j] += matriz_1[i][k] * matriz_2[k][j]

  print("--------------------------------------------")
  print("Matriz producto")
  for m in range(len(matriz_producto)):                                        # Para imprimir la segunda matriz con forma de matriz ;)
    print(matriz_producto[m])

if __name__ == "__main__":
  matriz_1=[]                                                                  # Se crea la matriz vacía
  matriz_2=[]                                                                  # Se crea la matriz vacía
  matriz_producto = []                                                         # El resultado de la operacion
  CrearMatriz(matriz_1, matriz_2)                                              # Se llama la función para crear la matriz
```
**3.** Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
* EXPLICACIÓN
* Mirar archivo Punto_3.py
```pseudocode
def CrearMatriz(matriz):                                                      # Para que el usuario cree la matriz
  fila=[]
  filas=int(input("Ingrese el número de filas: "))                            # Ingresar el número de filas que quiere
  columnas=int(input("Ingrese el número de columnas: "))                      # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
  for i in range(filas):                                                      # Para ir creando cada fila
    for j in range(columnas):                                                 # Para añadir los valores de la fila (cada columna)
      valor=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila.append(valor)                                                      # Se añade el valor a la fila
    matriz.append(fila)                                                       # Se añade la fila terminada a la matriz
    fila=[]                                                                   # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")
  print("Matriz original")
  for k in range(len(matriz)):                                                # Para imprimir la matriz con forma de matriz ;)
    print(matriz[k])

def MatrizTranspuesta(matriz, matriz_transpuesta):                            # Función para crear la matriz transpuesta
    filas = len(matriz)                                                       # Para definir su tamaño según la original
    columnas = len(matriz[0])                                                 # Para definir su tamaño según la original

    for j in range(columnas):                                                 # Empieza tomando las columnas
        fila_transpuesta = []                                                 # La coloqué aquí para que cuando se repita el for no se acumulen valores
        for i in range(filas):                                                # Toma la fila
            fila_transpuesta.append(matriz[i][j])                             # Ubica el elemento en esa ubicación "invertida"
        matriz_transpuesta.append(fila_transpuesta)                           # Se añade la fila que se intercambió

    print("--------------------------------------------")
    print("Matriz transpuesta")
    for k in range(len(matriz_transpuesta)):                                  # Para imprimir la matriz transpuesta con forma de matriz ;)
      print(matriz_transpuesta[k])

if __name__ == "__main__":
  matriz=[]
  matriz_transpuesta=[]                                                       # Se crea la matriz vacía
  CrearMatriz(matriz)                                                         # Se llama la función para crear la matriz
  MatrizTranspuesta(matriz, matriz_transpuesta)                               # Se llama la función para la matriz transpuesta
```
**4.** Desarrollar un programa que sume los elementos de una columna dada de una matriz.
* EXPLICACIÓN
* Mirar archivo Punto_4.py
```pseudocode
def CrearMatriz(matriz):                                                     # Para que el usuario cree la matriz
  fila=[]
  filas=int(input("Ingrese el número de filas: "))                           # Ingresar el número de filas que quiere
  columnas=int(input("Ingrese el número de columnas: "))                     # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
  for i in range(filas):                                                     # Para ir creando cada fila
    for j in range(columnas):                                                # Para añadir los valores de la fila (cada columna)
      valor=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila.append(valor)                                                     # Se añade el valor a la fila
    matriz.append(fila)                                                      # Se añade la fila terminada a la matriz
    fila=[]                                                                  # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")
  for k in range(len(matriz)):                                               # Para imprimir la matriz con forma de matriz ;)
    print(matriz[k])

def SumaColumna(matriz):                                                     # Para sumar las columnas
  columna=[]
  suma=0
  print("--------------------------------------------")
  for i in range(len(matriz[0])):                                            # Estoy mirando el número de columnas
    for j in matriz:                                                         # Estoy tomando cada fila
      elemento=j[i]                                                          # Estoy tomando el valor de cada fila de la misma columna
      columna.append(elemento)                                               # Añado el elemento de cada columna a la lista de columna
    for k in columna:                                                        # Sumo los elementos de la columna que acabó de identificar
      suma+=k
    print("La suma de la columna " + str(i) + " es: " + str(suma))           # Muestro el resultado de la suma de esa columna
    suma=0
    columna=[]                                                               # Para que no se acumulen los valores de las demás columnas

if __name__ == "__main__":
  matriz=[]                                                                 # Se crea la matriz vacía
  CrearMatriz(matriz)                                                       # Se llama la función para crear la matriz
  SumaColumna(matriz)                                                       # Se llama la función para sumar las columnas
```
**5.** Desarrollar un programa que sume los elementos de una fila dada de una matriz.
* EXPLICACIÓN
* Mirar archivo Punto_5.py
```pseudocode
def CrearMatriz(matriz):                                                     # Para que el usuario cree la matriz
  fila=[]
  filas=int(input("Ingrese el número de filas: "))                           # Ingresar el número de filas que quiere
  columnas=int(input("Ingrese el número de columnas: "))                     # Ingresar el número de columnas que quiere
  print("--------------------------------------------")
  for i in range(filas):                                                     # Para ir creando cada fila
    for j in range(columnas):                                                # Para añadir los valores de la fila (cada columna)
      valor=int(input("Ingrese el valor de la fila " + str(i) + ": "))
      fila.append(valor)                                                     # Se añade el valor a la fila
    matriz.append(fila)                                                      # Se añade la fila terminada a la matriz
    fila=[]                                                                  # Se deja vacía la fila para seguir con las demás
  print("--------------------------------------------")
  for k in range(len(matriz)):                                               # Para imprimir la matriz con forma de matriz ;)
    print(matriz[k])

def SumaFila(matriz):                                                        # Para la suma de las filas
  suma=0
  print("--------------------------------------------")
  for i in matriz:                                                           # Selecciona la fila de la matriz
    for j in i:                                                              # Selecciona cada elemento de esa fila
      suma+=j                                                                # Suma los elementos
    print("La suma de la fila " + str(i) + " es: " + str(suma))
    suma=0

if __name__ == "__main__":
  matriz=[]                                                                 # Se crea la matriz vacía
  CrearMatriz(matriz)                                                       # Se llama la función para crear la matriz
  SumaFila(matriz)                                                          # Se llama la función para sumar las filas
```
