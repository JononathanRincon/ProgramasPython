def resultadoPrestamo(cantidad_meses, cuota_fija, amortizacion, interes_mensual, saldo):
    retorno_lista = []
    for j in range(cantidad_meses):
        retorno_lista.append([
            j+1,
            cuota_fija,
            amortizacion[j],
            interes_mensual,
            saldo[j]
        ])
    return retorno_lista