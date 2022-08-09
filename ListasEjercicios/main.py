# Crenado una lista 
"""["Hola", "Mundo"]
list(["Hola","Mundo"])
x = 10
print(type(x))
z = "Hola"
print(type(z))
y = 7.8
print(type(y))

lista = ["Hola", 1,True, 3.5]
print(type(lista))"""
"""
#Recorrer una lista
#          0 1 2 3 4 5    6
numeros = [1,2,3,4,5,6,[7,8,9,[10,11,12]]]
print(numeros[6][3][1])"""


# Metodos en las listas 

#Metodo append
"""nombre = ["Maria", "Pedro","Jose"]
print(nombre)
nombre.append("Cristian")
print(nombre)"""

#Mtodo extend

nombre1 = ["Maria", "Pedro","Jose"]

#nombre2 = ["Fabio","Teresa","Rocio"]

nombre1.extend(["Teresa","Rocio"])
print(nombre1)