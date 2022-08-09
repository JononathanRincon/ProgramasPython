from IPython.display import HTML, display
import tabulate

import entrada
import calculos
import resultados

def main():
    valor_prestamo, tasa_interes, numero_cuotas = entrada.entrada()

    interes_MV = calculos.mesVencido(tasa_interes) #calcula el valor del interés dado como Efectivo anual a Mes Vencido
    cuota_fija = calculos.cuota(numero_cuotas, valor_prestamo, interes_MV) #Calcula la cuota mensual fija (para todos los 𝑛 meses de      duración del préstamo). 
    amortizacion = calculos.amortizacion(cuota_fija, numero_cuotas, interes_MV) #Calcula el valor de la amortización al capital para el mes 𝑗, dado por 𝐴𝑚𝑜𝑟𝑡𝑖𝑧𝑎𝑐𝑖ó𝑛 𝑗=𝑐𝑢𝑜𝑡𝑎 𝑚𝑒𝑠 (𝑓𝑖𝑗𝑎)−𝑖𝑛𝑡𝑒𝑟é𝑠𝑗
    saldo = calculos.saldo(valor_prestamo, amortizacion, numero_cuotas) #Calcula el saldo a deber en el mes 𝑗, dado por: 𝑆𝑎𝑙𝑑𝑜𝑗=𝑆𝑎𝑙𝑑𝑜𝑗−1−𝐴𝑚𝑜𝑟𝑡𝑖𝑧𝑎𝑐𝑖ó𝑛 𝑗.

    resultadoData = resultados.resultadoPrestamo(numero_cuotas, cuota_fija, amortizacion, interes_MV, saldo) #muestra el resultado de los cálculos realizados
    display(HTML(tabulate.tabulate(resultadoData, tablefmt='html', headers=["Periodo", "Cuota fija", "Amortización Capital", "Intereses", "Saldo"], floatfmt=".2f")))