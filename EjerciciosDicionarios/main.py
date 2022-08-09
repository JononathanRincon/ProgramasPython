"""#formas de crear un diccionario
diccionario = dict()
print(type(diccionario))

diccionario2 = {}
print(type(diccionario2))
#agregar un elemtento al diccionario
numeros = {"one":"uno","two":"dos","three":"tres"}
print(numeros)

diccionario2 = {}
print(diccionario2)
diccionario2["Hola"]="Mundo"
print(diccionario2)

#modificando elelemtos en un diccionario

l = [1,2,3]
l[0]="uno"
print(l)

numeros["one"] = 1
print(numeros)
print(numeros["two"])

pantalones = {"Mocho":30, "Jean":32, "sudadera":"L"}
print(pantalones)
#print(pantalones["suda"])
print(len(pantalones))

pantalones = {"persona":{"edad":"estaruta"}, "Jean":32, "sudadera":"L"}
print(pantalones["persona"])

numeros= {1:"uno",2:"dos",3:"tres"}
print(1 in numeros)
print(numeros[1])"""

#Metodos en diccionarios

"""contenedor = list(numeros.values())
print(contenedor)
print(contenedor[0])"""

"""numeros= {1:"uno",2:"dos",3:"tres", 4:"cuatro", 5:"cinco",6:"seis"}
print(numeros)
#Metodo clear 
numeros.clear()
print(numeros)

numeros[7]="siete"
print(numeros)

#metodo fromkeys

l = [1,2,3,4]
numeros = dict.fromkeys(l)
print(numeros)
numeros[1]="Uno"
numeros[2]="Dos"
numeros[3]="Tres"
numeros[4]="Cuatro"
print(numeros)
"""
"""#Metodo copy 
numeros= {1:"uno",2:"dos",3:"tres", 4:"cuatro", 5:"cinco",6:"seis"}
print(numeros)
print(id(numeros))
print("\n")
datos = numeros.copy()
print(datos)
print(id(datos))
print("\n")
datos2 = numeros
print(id(datos2))
print(datos2)
numeros[7]="siete"
print(datos2)"""
"""#Metodo setdefault
numeros= {1:"uno",2:"dos",3:"tres", 4:"cuatro", 5:"cinco",6:"seis"}
print(numeros)
print("\n")
clave=numeros.setdefault(7, "siete")
print(numeros)"""
#metodo update

"""diccionario1 = {1:"uno",2:"dos",3:"tres"}
diccionario2 = {4:"cuatro", 5:"cinco",6:"seis"}
print(diccionario1)
print(diccionario2)
diccionario3 = {12:"doce"}
print("\n")
diccionario1.update(diccionario2)
print(diccionario1)
print("\n")
diccionario1.update({9:"nueve",10:"diez"})
print(diccionario1)
print(diccionario2)"""

#Metodo get
diccionario1 = {1:"uno",2:"dos",3:"tres"}
print(diccionario1[1])
#print(diccionario1.get(1))
#print(diccionario1[1])

"""#operador in para verificar si existe llave 
diccionario1 = {1:"uno",2:"dos",3:"tres"}
existe = 1 in diccionario1
print(existe)
"""
# metodo para obtener llaves y valores de un dicionario items


"""numeros = {1:"uno",2:"dos",3:"tres"}
for k, v in numeros.items():
  print("la llave es:", k, "y el valor es:", v)

claves = numeros.keys()
print(claves)
valores = numeros.values()
print(valores)

print(len(numeros))"""
"""
numeros = {1:"uno",2:"dos",3:"tres"}
for llave in numeros:
  print("la llave es:",llave, "y el valor es:",numeros[llave])
"""
#  1   "uno"
#
#Ejercicio ingresando elemetos desdde input a diccionario

def proveedor():
  productos = {}
  for x in range(2):
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el valor de producto: "))
    productos[nombre]=precio
  return productos

print(proveedor())