from calculadora.tarjeta import Tarjeta
from calculadora.tarjeta_servicios import Tarjeta_Servicios
from calculadora.usuario import Usuario

tarjeta = Tarjeta()
datos = tarjeta.crea_tarjeta()
tarjeta.generar_reporte(datos)
tarjeta.pago_recurrente(datos)
tarjeta.pagos_diferentes(datos)
tarjetas = ["852369","458792"]
user = Usuario("Marlon",tarjetas)
user.añadir_tarjetas()
user.lista_tarjetas()
print(user)

datos = {}
tarjeta_s=Tarjeta_Servicios(datos)
tarjeta_s.crea_tarjeta()
tarjeta_s.captura_nueva_deuda()
tarjeta_s.pagos_diferentes()





