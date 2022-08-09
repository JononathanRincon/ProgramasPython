import random as r
import pandas as pd

def PreguntaXMesesFiltrados(string):
  print('') 
  if string == "2":
    print(CrearSeries())
  print()
  print("Ingrese el rango de años que desea filtrar la busqueda")
  pre1 = int(input("desde el año "))
  pre2 = int(input("hasta el año "))
  if string == "1":
    CrearListas(pre1, pre2)  
  if string == "2":
    RealizarFiltro(pre1, pre2) 
  
def CrearListas(pre1, pre2):
  listaCreadaFechas = crearListasYear(pre1, pre2)
  listaCreadaVentas = CrearListaDeVentas(len(listaCreadaFechas))
  CrearModeloDataFrame(listaCreadaVentas,listaCreadaFechas)
  
def crearListasYear(pre1, pre2):
  listaAnos = list(range(pre1, pre2+1))
  return listaAnos
  
def CrearListaDeVentas(rango):
  ListaVentas = r.sample(range(1000,5000), rango)
  return ListaVentas
  
def CrearModeloDataFrame(listaCreadaVentas,listaCreadaFechas):
  #print(listaCreadaVentas," \n",listaCreadaFechas)
  Ventas = pd.Series(data=listaCreadaVentas,index= listaCreadaFechas) 
  DataFrameVenta = pd.DataFrame({'Venta':Ventas})
  DataFrameVenta['Menos 10%'] = DataFrameVenta.Venta - ((DataFrameVenta.Venta*10)/100)
  print()
  print(DataFrameVenta)
  print()

def CrearSeries():   
  ventasAnual = pd.Series([4518, 2138, 4161, 2201, 4882, 4087, 1219, 2105, 1123, 2626, 4165, 2052, 4791, 1018, 2305, 1991, 3438, 4997])
  years = pd.Series([2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,2016,2017,2018, 2019,2020,2021,2022])
  Ventas = pd.DataFrame({'Años':years, 'Ventas':ventasAnual})  
  return Ventas

def RealizarFiltro(pre1, pre2):
  Ventas = CrearSeries();
  print()    
  Ventas['Menos 10%'] = Ventas["Ventas"] - ((Ventas["Ventas"]*10)/100)
  resultado = (Ventas["Años"] >= pre1) & (Ventas["Años"]<= pre2) 
  resultado = Ventas.loc[resultado]
  imprimirDataFrame(resultado)
  
def imprimirDataFrame(resultado):
  print(resultado)
  print("\n")
  

