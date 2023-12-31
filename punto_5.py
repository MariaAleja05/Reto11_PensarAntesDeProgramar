# -*- coding: utf-8 -*-
"""Punto_5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

##**Punto 5**
"""

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