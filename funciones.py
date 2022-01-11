def crea_tarjeta():
    datos = {}
    n_tarjeta=input("Inserte su nombre de tarjeta: ")
    t_interes=int(input("Inserte tasa de interes: "))
    deuda=int(input("Ingrese su deuda actual: "))
    pago=int(input("Inserte el pago que desea realizar: "))
    cargos=int(input("Ingrese los nuevos cargos a su tarjeta: "))

    if pago>deuda:
        print("\nusuario con tarjeta: {}".format(n_tarjeta))
        print("No se puede realizar un pago mayor al total de la deuda pasada")
    else:
        datos["num_tarjeta"]=n_tarjeta
        datos["t_interes"]=t_interes
        datos["deuda"]=deuda
        datos["pago"]=pago
        datos["cargos"]=cargos
    
    return datos

def captura_nueva_deuda(tarjeta_data):
    interes_mensual= tarjeta_data["t_interes"]/12
    deuda_recalculada = (tarjeta_data["deuda"]-tarjeta_data["pago"])*(1+interes_mensual)
    tarjeta_data["nueva_deuda"]= deuda_recalculada + tarjeta_data["cargos"]

    return tarjeta_data

def generar_reporte(tarjeta_data):
    print("\n")
    for k,v in tarjeta_data.items():
        print("{} : {}".format(k,v))

def lista_tarjetas(tarjetas):
    for tarjeta in tarjetas:
        captura_nueva_deuda(tarjeta)
        generar_reporte(tarjeta)

def pago_recurrente(tarjeta_data):
    mes = 1
    while tarjeta_data["deuda"]>0:
        print(mes)
        generar_reporte(tarjeta_data)
        tarjeta_data["deuda"] = (tarjeta_data["deuda"]-tarjeta_data["pago"])
        mes+=1