""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya
    Abril 2022 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma de 4 numeros: (1)")
  print("==================================================")
  print("| 2. Calcular la resta de 4 numeros: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación de 4 numeros: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular división de 4 numeros: (3)")
  print("==================================================")
   
  opcion = input()
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion=menu_operaciones()

def realizarOperacion():
  count = 0
  if operacion == "1":
    count = 1 + count
    num = int(input("Ingrese el numero {count} :"))
    count = 1 + count
    num1 = int(input("Ingrese el numero {count} :"))
    count = 1 + count
    num2 = int(input("Ingrese el numero {count} :"))
    count = 1 + count
    num3 = int(input("Ingrese el numero {count} :"))
    calc.sumar_numeros(num, num1, num2, num3)
      
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


    
       
      
  
  
  
