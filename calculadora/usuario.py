from calculadora.tarjeta import captura_nueva_deuda, generar_reporte
def lista_tarjetas(tarjetas):
    """Función que imprime datos de diferentes tarjetas"""
    for tarjeta in tarjetas:
        captura_nueva_deuda(tarjeta)
        generar_reporte(tarjeta)