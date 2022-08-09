"""# grafica de ejes x,y
import matplotlib.pyplot as plt
# pais 1 
x = [2016, 2017, 2018, 2019, 2020, 2021] # vector años 
y = [42, 43, 45, 47, 48, 49] #vector poblacion

#pais 2
x2 = [2016, 2017, 2018, 2019, 2020, 2021] # vector años 
y2 = [43, 43, 44, 44, 45, 45] #vector poblacion

plt.xlabel("Años")
plt.ylabel("poblacion(M)")
plt.title("Años vs Poblacion")
# plotting
plt.plot(x, y, marker ='o', linestyle='--', color = 'r', label="Colombia")
plt.plot(x2, y2, marker='d', linestyle='-', color = 'g', label="Brasil" )
plt.legend()
plt.show()"""

"""# Crando graficas de barras

x = ["Colombia", "Brasil","Argentina"] # paises
y = [40, 50, 35]

plt.bar(x,y, color = 'r')
plt.title("Años vs Paises")
plt.xlabel("Paises")
plt.ylabel("Años")
plt.show()"""

"""#creando graficas de pastel
x = ["Colombia", "Brasil","Argentina"] # paises
y = [40, 50, 35]

plt.pie(y, labels =x, autopct='%.0f %%')# muestre el procentaje al lado de los numeros
plt.show()"""