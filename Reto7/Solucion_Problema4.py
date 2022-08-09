
import pandas as pd


def CrearDiccionario():
  estudiantes = {
    "Estudiante 1":[3,5,2,5],
    "Estudiante 2":[5,4,5,4],
    "Estudiante 3":[2,3,4,1],
    "Estudiante 4":[4,2,4,1]
  }
  estudiantesSeries = pd.DataFrame(estudiantes)
  print(estudiantesSeries)
  lista1 = estudiantesSeries.min()
  lista2 = estudiantesSeries.max()
  lista3 = estudiantesSeries.std()
  lista4 = estudiantesSeries.mean()
  tablaDicionario = {
    "Minima":lista1,
    "Maxima":lista2,
    "Desviacion Estandar":lista3,
    "Media":lista4
  }
  tabla = pd.DataFrame(tablaDicionario)
  print(tabla)
  return lista1,lista2, lista3, lista4
  
    
