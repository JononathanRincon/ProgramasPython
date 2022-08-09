import pandas as pd

def CrearDataFrame():  
  columna = {
    "mes": ["enero","febrero","marzo","abril"],
    "ventas":[30500,35600,28300,33900],
    "Gastos":[22000,23400,18100,20700]
  }
  problema_1 = pd.DataFrame(columna)
  print(problema_1)
  return problema_1
  




