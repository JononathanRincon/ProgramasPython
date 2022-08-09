import pandas as pd
"""
elementos = {
    "Numero Atomico":[1, 6, 47, 88],
    "Masa Atomica":[1.008, 12.011, 107.87, 226],
    "Familia":["No metal", "No metal", "Metal", "Metal"]
}

tabla_periodica = pd.DataFrame(elementos)
print(tabla_periodica)

# Creando DataFrames a partir de listas

unidades_datos = [[2, 5, 3, 2], 
                  [4, 6, 7, 2], 
                  [3, 2, 4, 1]]

unidades = pd.DataFrame(unidades_datos, index=[2015, 2016, 2017], columns=["Ag", "Au", "Cu", "Pt"])
print(unidades)"""

"""# crear un DataFrame en base a varios diccionarios

unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2} 
unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1} 

unidad = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017], index=[2015, 2016, 2017])
print(unidad)"""

"""# crear un DataFrame en base a varios diccionarios

unidades_2015 = {"Ag":2, "Au":5, "Cu":3, "Pt":2} 
unidades_2016 = {"Ag":4, "Au":6, "Cu":7, "Pt":2}
unidades_2017 = {"Ag":3, "Au":2, "Cu":4, "Pt":1} 

unidad = pd.DataFrame([unidades_2015, unidades_2016, unidades_2017], index=[2015, 2016, 2017])
print(unidad)"""
"""# Metodos en DataFrame head, tail, sample


entradas = pd.Series([11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12], 
                     index=["ene","feb","mar","abr","may","jun","jul",
                            "ago","sep","oct","nov", "dic"])

salidas = pd.Series([9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14],
                   index=["ene","feb","mar","abr","may","jun","jul",
                            "ago","sep","oct","nov", "dic"] )
"""
almacen = pd.DataFrame(
  {"Entradas":entradas,
  "Salidas":salidas}
)
almacen["Neto"] = almacen.Entradas - almacen.Salidas

print(almacen)
print("\n")
print(almacen.head())
print("\n")
print(almacen.head(5))
print("\n")
print(almacen.tail())
print("\n")
print(almacen.tail(2))
print("\n")
print(entradas.sample(3))
print("\n")
print(almacen.sample(3))"""


#Metodos en DataFrame describe, 
entradas = pd.Series([11, 18, 12, 16, 9, 16, 22, 28, 31, 29, 30, 12], 
                     index=["ene","feb","mar","abr","may","jun","jul",
                            "ago","sep","oct","nov", "dic"])

salidas = pd.Series([9, 26, 18, 15, 6, 22, 19, 25, 34, 22, 21, 14],
                   index=["ene","feb","mar","abr","may","jun","jul",
                            "ago","sep","oct","nov", "dic"] )

almacen = pd.DataFrame({"Entradas":entradas, "Salidas":salidas})
almacen["Neto"] = almacen.Entradas - almacen.Salidas

print(almacen)
print("\n")
print(almacen.describe())
print("\n")
almacen.info()"""
"""# Implementado metodo values_count para series

import numpy as np

s = pd.Series([3, 1, 2, 1, 1, 4, 1, 2, np.nan])
print(s)
print("\n")
print(s.value_counts())
print("\n")
print(s.value_counts(dropna= False))"""