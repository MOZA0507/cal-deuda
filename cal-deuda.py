from funciones import crea_tarjeta, captura_nueva_deuda, generar_reporte, lista_tarjetas, pago_recurrente

datos = crea_tarjeta()
datos = captura_nueva_deuda(datos)
generar_reporte(datos)
lista_tarjetas([{'num_tarjeta':'4582','t_interes': 5, 'deuda':1500,'pago':800,'cargos':1000},
{'num_tarjeta':'4582','t_interes': 4, 'deuda':1800,'pago':900,'cargos':1000}])
pago_recurrente(datos)