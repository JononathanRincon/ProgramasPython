""" Programa ventas 
    Programa para el manejo de vacunados por mes
    incorpora al modulo vacunas.py
Realizado por Jonathan Andres Rincon Ruiz
    """

#---------------- Zona librerias------------
import vacunas as vt

cantidadVacunados= int(input("Ingrese el numero de los vacunadores: "))
arraY = vt.leer_numero_empleados(cantidadVacunados)
aryv = vt.leer_ventas_empleados_mes(arraY)
ary = vt.ordenar_vendeores_por_ventas(arraY)
ary2 = vt.calcular_cinco_vendedores(ary)
vt.calcula_mes_mas_ventas(aryv)
vt.greficar_ventas_por_mes(aryv)

  
  
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================