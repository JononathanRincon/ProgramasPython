def mesVencido(interes_anual):
    return interes_anual / 12

def cuota(numero_meses, valor_prestamo, interes_mensual):
    interes_mensual = interes_mensual / 100
    return (valor_prestamo*(interes_mensual*(1+interes_mensual)**numero_meses)) / ((interes_mensual+1)**numero_meses - 1)

def amortizacion(cuota_mes, numero_meses, interes_mensual):
    amortizacion_retorno = []
    for j in range(numero_meses):
        amortizacion_retorno.append(cuota_mes - (cuota_mes * interes_mensual / 100))
    return amortizacion_retorno

def saldo(valor_prestamo, amortizacion, cantidad_meses):
    saldo_retorno = [valor_prestamo]
    for j in range(cantidad_meses - 1):
        if j == cantidad_meses - 2:
            saldo_retorno.append(saldo_retorno[j] - saldo_retorno[j])
        else:
            saldo_retorno.append(saldo_retorno[j] - amortizacion[j])
    return saldo_retorno