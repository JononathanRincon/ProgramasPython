""" Modulo Ciclos
    Funciones para practicas con ciclos
    Oscar Franco-Bedoya
    Abril-2022 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def simulador_movimiento(a,t):
  #TODO Comentar código
  #TODO Implementar la función
  d = 0
  s =0
  while s<t:
    s = s+1
    d=a*s
    print("la distancia recorrida en metros es", d,"el tiempo transcurrido ",s,"segundos")
  return d

def calculador_series(n):
  comprobar = True 
  #creamos variable comprobar y le damos valor de verdad. 
  while comprobar == True: 
    # creamos un ciclo while, que mientras comprobar sea true se repita el ciclo.
    n = int(input("ingrese un numero entero positivo :"))
    #creamos una variable n que va a ingresar un entero.
    #creamos la condicional if, que si n es mayor que 0 se ejecute el ciclo for.
    if n > 0:
      resultado = 0
      #En el ciclo for cuando i esta en rango de 1 hasta       #n+1 se ejecutara hasta n veces colocadas.
      for i in range (1,n+1): 
        #el resultado sera igual al resultado mas el ciclo       #de iteracion en el ciclo for, dumandole (1/i)
        resultado = resultado + (1/i)
        #imprimimos el resultado  en pantalla.
        print ("el resultado de la serie es:", resultado)
      else:
        print("no es correcto el numero")
  
      return


def constructor_triangulos (t):
 # n=int(input("ingrese un numero"))
  #ingresar un numero el cual se va a guardar como un entero.
  for i in range (1,t+1):
    for J in range (1,i+1):
      print(J+i-1, end =" ")
    print(" ")
        #fin XD
    #TODO Implementar la función
  return 