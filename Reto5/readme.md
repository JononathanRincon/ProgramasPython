
# Reto 5
# Codificando el Mensaje
En un episodio de CSI un capo de la mafia diseño un interesante método para evitar que sus mensajes fueran descubiertos. El método se llamaba *Código de Rotación*

Es una estrategia simple e ingeniosa, cada letra es cambiada por la cuarta letra en su orden alfabetico como lo muestra las siguientes litas

- A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
- D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C

Así cuando se pasaba un mensaje primero se pasaba a mayúsculas y luego se codificaba 

por ejemplo
--
*cuidado esta noche*
--

el mensaje codificado es

--
*FXLGDGR HVWD QRFKH*
--

## ¿Que debo hacer?

Tu misión es muy sencilla, implementar una funció que codifique y decodifique mensajes utilizando la estrategia *Código de Rotación*

### Tips
*   Utilice diccionarios para resolver este ejercicio
* En el archivo csi.py esta la línea base para implementar esta función.


