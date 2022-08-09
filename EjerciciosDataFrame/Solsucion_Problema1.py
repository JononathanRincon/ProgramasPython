import pandas as pd

def Crear_DataFame ():
  ventas = pd.Series([30500, 35600, 28300, 33900],
                     index=['Enero', 'Febrero', 'Marzo',
                            'Abril'])

  gastos = pd.Series([22000, 23400, 18100, 20700],
                     index=['Enero', 'Febrero', 'Marzo',
                            'Abril'])

  almacen = pd.DataFrame({'Ventas':ventas,
                          'Gastos':gastos})
  print(almacen)
  return almacen