"""#Creando una tupla
#primera forma de crear tuplas
#    0   1      2   3     4
t = (1,"Hola",True,1.7,[4,5,6])
#                       0 1 2
print(t[4][0])
t = ()
print(type(t))
#Segunda forma de crear una tupla
t = tuple(("Hola_mundo"))
print(type(t))
#tercera forma para crear una tupla
t = 1,"Hola", True,1.7,[4,5,6]
print(type(t))
#Intentado modificar una tupla
l = [1,2,3,4,5,6,7,8]
print(l)
l[0]="m"
print(l)
#Intentando modificar 
t = (1,2,3,4,5,6,7,8)
print(t)
t[0]="m"
print(t)"
#Creando tuplas de un solo elemento
t = ("Hola",)
print(type(t))
#Creando rebanadas en las tuplas 
t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(t[7:14])
print(t[2:8])

#Sumando tuplas

tu = "a","b","c","d"
t = ("A",) + tu[2:]
print(t)
print(tu)

#Comparando tuplas

print((0, 1, 2) < (0, 3, 4))
print((0, 3, 2000000) < (0, 3, 4))"""

#Asigancion y Desempaquetado

a,b = 2,1
print(a)
print(b)
b,a = a,b
print(a)
print(b)

tupla = (1,2,3,4)
print(tupla)
a,b,c,d = tupla
print(a)
print(b)
print(c)
print(d)
print(a + b)
print(tupla)