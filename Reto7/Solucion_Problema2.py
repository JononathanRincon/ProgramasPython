
#import pandas as pd

def añadirBalance(dataFrame):
  print('\n')
  dataFrame['Balance'] = dataFrame.ventas - dataFrame.Gastos
  print(dataFrame)
  print('\n')