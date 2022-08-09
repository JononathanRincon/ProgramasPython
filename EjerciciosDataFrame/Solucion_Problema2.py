import pandas as pd

def añadir_balance(DataFrame):
  DataFrame['Balance'] = DataFrame.Ventas - DataFrame.Gastos
  print(DataFrame)
  print('\n')