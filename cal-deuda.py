from calculadora.tarjeta import Tarjeta
from calculadora.tarjeta_servicios import Tarjeta_Servicios
from calculadora.usuario import Usuario

datos = {}
tarjeta = Tarjeta(datos)
tarjeta.crea_tarjeta()
tarjeta.generar_reporte()
tarjeta.crear_csv_tarjeta()
tarjeta.crear_json()
tarjeta.json_a_dic()
#tarjeta.pago_recurrente()
#tarjeta.pagos_diferentes()

"""tarjetas = ["852369","458792"]
user = Usuario("Marlon",tarjetas)
user.añadir_tarjetas()
user.lista_tarjetas()
user.crear_csv()
print(user)"""

"""datos = {}
tarjeta_s=Tarjeta_Servicios(datos)
tarjeta_s.crea_tarjeta()
tarjeta_s.captura_nueva_deuda()
tarjeta_s.pagos_diferentes()"""





