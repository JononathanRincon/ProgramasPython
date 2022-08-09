""" Modulo para la codificación y decodificación de
    mensajes 
     """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def ConvertirMensajeEnMayuscula(mensaje):
  return mensaje.upper()


def codificar_mensaje(MensajeMayus):
  Diccionario = {'Abecedario':['A','B','C','D','E','F','G','H',
                               'I','J','K','L','M','N','O','P','Q',
                               'R','S','T','U','V','W','X','Y','Z']}
  
  LongitudMensaje = len(MensajeMayus)
  mensajeCodificado = ""
  countMen =0  
  for j in range(0,LongitudMensaje): 
    espacio = 0
    for i in range(0, 26): 
      if MensajeMayus[countMen] == Diccionario['Abecedario'][i]:
        espacio = i + 3
        if espacio > 25:
          espacio = espacio - 26           
        mensajeCodificado = mensajeCodificado + Diccionario['Abecedario'][espacio] 
    if not(Noencontro(Diccionario['Abecedario'][0:26], MensajeMayus[countMen])):
      mensajeCodificado = mensajeCodificado + " "
    countMen = countMen + 1
      
  return mensajeCodificado


def Noencontro(var, b):
  for a in var:
    #print(a,"1",b)
    if a == b:
      return True
  return False
  
def decodificar_mensaje(mensaje_codificado):
  Diccionario = {'Abecedario':['A','B','C','D','E','F','G','H',
                               'I','J','K','L','M','N','O','P','Q',
                               'R','S','T','U','V','W','X','Y','Z']}
  
  LongitudMensaje = len(mensaje_codificado)
  mensajeCodificado = ""
  countMen =0  
  for j in range(0,LongitudMensaje): 
    espacio = 0
    for i in range(0, 26): 
      if mensaje_codificado[countMen] == Diccionario['Abecedario'][i]:
        espacio = i - 3
        if espacio < 0:
          espacio = espacio + 26           
        mensajeCodificado = mensajeCodificado + Diccionario['Abecedario'][espacio]  
    if not(Noencontro(Diccionario['Abecedario'][0:26], mensaje_codificado[countMen])):
      mensajeCodificado = mensajeCodificado + " "    
    countMen = countMen + 1
  return mensajeCodificado

