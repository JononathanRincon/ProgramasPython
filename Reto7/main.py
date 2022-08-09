import Solucion_Problema1 as sp1
import Solucion_Problema2 as sp2
import Solucion_Problema3 as sp3
import Solucion_Problema4 as sp4
import Solucion_Problema5 as sp5

opc = 0
a,e,i,o = 0,0,0,0
almacenarDatafreme = []
while (opc != 6):
  print("Menu reto 7")
  print("1. Ingrese al problema 1")
  print("2. Ingrese al problema 2")
  print("3. Ingrese al problema 3")
  print("4. Ingrese al problema 4")
  print("5. Ingrese al problema 5")
  print("6. Salir")
  opc = int(input("Ingrese la opcion "))
  if opc == 1:    
    print("\n")
    almacenarDatafreme = sp1.CrearDataFrame()
    print("\n")
  if opc == 2:
    sp2.añadirBalance(almacenarDatafreme)
  if opc == 3:
    opc2 = input("\nEscoja una opcion\n1. asignar valores a ventas aletoriamente\n2. DataFrame lleno\nDigite la opcion: ")
    if opc2 == "1":
      sp3.PreguntaXMesesFiltrados("1")
    if opc2 == "2":
      sp3.PreguntaXMesesFiltrados("2")
  if opc == 4:
   a,e,i,o = sp4.CrearDiccionario()
  if opc == 5:
    sp5.ImportarDatos(a,e,i,o)
      
    
    
    



  

  