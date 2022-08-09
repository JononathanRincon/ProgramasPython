""" Programa Codificando el Mensaje
    Realiza codificación y decodificación 
    de mensajes
    incorpora al modulo csi.py
    Realizado por: Jonathan Andres Rincon Ruiz
    Grupo 35
     """

#---------------- Zona librerias------------
import csi as sh

def main():
  opc = 1
  mensaje = ""
  while(opc != 3):
    print("------Menu------")
    print("1.codifique ")
    print("2.descodifique")
    print("3.Salir")
    opc = int(input("Ingrese una opcion:  "))
    if opc == 1:
      Mensaje = input("Ingrese el mensaje que desea codificar:  \n\t\t [ ")
      MensajeMayus = sh.ConvertirMensajeEnMayuscula(Mensaje)
      mensaje = sh.codificar_mensaje(MensajeMayus)
      print("\nEl mensaje codificado es \n\n >>",mensaje,"<< \n\n")
    if opc == 2:
      mensajeDescodificado = sh.decodificar_mensaje(mensaje)
      print("\nEl mensaje descodificado es: \n\n >>",mensajeDescodificado,"<< \n\n")
    if opc == 3:
      print("Escogio la opcion de salir. Hasta Luego")

main()
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

