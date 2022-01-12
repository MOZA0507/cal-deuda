from calculadora.tarjeta import Tarjeta
from calculadora.tarjeta import Tarjeta
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


