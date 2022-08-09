# Creando Matrices  3 X 3
#     0  1   2
"""m = [[1, 4, 5], # 0 
    [-5, 8, 9], # 1
    [10,11,12]] # 2
#Acceder a los elemntos de una matriz
print(type(m))
print(m[1][2])
print(m[1][1])
print(m[2][0])
print(m[0][2])
print(m[1][0])
print(m[0][1])
print(m[0])
print(m[1])
print(m[2])
print(m)"""

#estructura de datos matricial
"""int = enteros
float = flotantes
str = cadenas
bool = booleanos
dict = diccionarios
list = listas
tuple = tuplas
  = matrices 
"""

"""import numpy as np
#          0    1   2
matriz = [[21, 22, 23], # 0
          [34, 35, 36], # 1
          [47, 48, 49] #  2
         ]
print(matriz)
print("\n")
matriz_np = np.array(matriz)
print(matriz_np)
print("\n")
f = int(input("Ingrese el valor de la Fila a obtener: "))
c = int(input("Ingrese el valor de la Columna a obtener: "))

fila = matriz_np[f,:]
columna = matriz_np[:,c]

print(fila)
print(columna)
"""
# ingresar dos datos demanera dinamica en la cual ustes puedan solicitarle al usuario obtener tanto la fila como la columna de la matriz

#recorrer matricez irregulares
import numpy as np 

matriz_irregular = [
#  0    1   2   3
  [21, 22, 23, 24], # 0
  [34, 35],         # 1
  [47, 48, 49]      # 2
]

matriz_irregular_np = np.array(matriz_irregular, dtype=object)


i = 3 # columna que queremos obtener

columna = []

for fila in matriz_irregular_np:
  if i < len(fila):
    columna.append(fila[i])
    
print(columna)
"""

#24
# modificar el codigo de tal manera que se puedan obetner la filas de la matriz

# sumar todo los elememstos de una matriz 
matriz = [[21, 22, 23], # 0
          [34, 35, 36], # 1
          [47, 48, 49] #  2
         ]

matriz_np = np.array(matriz)
print(matriz_np)
print("\n")
print(np.sum(matriz_np))
print("\n")
#sumando solo una fila de la matriz

print(np.sum(matriz_np, axis = 1)) #sumando filas
print(np.sum(matriz_np, axis = 0)) #sumar las columnas
"""
#  concatenando matrices

"""m1 = [[1,2,3],
      [4,5,6]]

m2 = [[7,8,9],
     [10,11,12]] 

m1_np = np.array(m1)
m2_np = np.array(m2)
print(m1_np)
print("\n")
print(m2_np)
print("\n")
print(np.concatenate((m1_np,m2_np), axis = 0))
print("\n")
print(np.concatenate((m1_np,m2_np), axis = 1))"""
""""
#multiplicando matricez

m = np.array([[1,2,3],
              [4,5,6]])

v = np.array([[1,2,3]])
print("\n")
print( m * v)"""
