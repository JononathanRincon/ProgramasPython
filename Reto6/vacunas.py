""" Modulo Vacunadores
    Funciones para el manejo de vacunas mensuales
    con matrices
    Oscar Franco-Bedoya
   Abril-2022 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
import numpy as np

def leer_numero_empleados(num):
  array = np.random.randint(10,300, size=(num, 12))
  count = 1
  print("\nLista de vendedores con sus ventas mensuales\n")
  for v in array: 
    print("vacunador ",count," ", v)
    count = count + 1
  return array

def leer_ventas_empleados_mes(arrays):
  array = np.array(arrays)  
  VentasMensuales = np.sum(array, axis = 0)
  print("\ntotal de Ventas por cada mes\n")
  print(VentasMensuales)
  return VentasMensuales

def ordenar_vendeores_por_ventas(arrays):
  array = np.array(arrays)  
  VendedoresXVentas = np.sum(array, axis = 1)
  SortVentasVendedores = np.sort(VendedoresXVentas, axis=None)
  print("\nTotal de ventas por vacunador organizadas")
  print("\n ",SortVentasVendedores)
  return SortVentasVendedores

def calcular_cinco_vendedores(arrays):
  array = np.array(arrays) 
  sorted_index_array = np.argsort(array)  
  sorted_array = array[sorted_index_array] 
  n = 5
  rslt = sorted_array[-n : ] 
  print("\n{} mejores vacunadores con ventas de: ".format(n), rslt) 
  return rslt

def calcula_mes_mas_ventas(arrays):
  array = np.array(arrays) 
  max_value = np.max(array)
  print('\nEl mes con mayor venta es:',max_value)
  return max_value
  
import matplotlib.pyplot as plt
def greficar_ventas_por_mes(arrays):
  meses = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
  mapeado = range(len(meses))  
  array = np.array(arrays)  
  plt.plot(array,'-',marker="o", markersize="8", markeredgewidth="2",
         markerfacecolor="green", markeredgecolor="white")
  plt.xticks(mapeado, meses)
  plt.grid()  
  plt.xlabel('Meses')
  plt.title('Cantidad de ventas por mes')
  plt.show()
  