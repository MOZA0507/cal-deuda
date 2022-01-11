n_tarjeta=input("Inserte su nombre de tarjeta: ")
t_interes=int(input("Inserte tasa de interes: "))
deuda=int(input("Ingrese su deuda actual: "))
pago=int(input("Inserte el pago que desea realizar: "))
cargos=int(input("Ingrese los nuevos cargos a su tarjeta: "))

interes_mensual= t_interes/12
deuda_recalculada = (deuda-pago)*(1+interes_mensual)
nueva_deuda = deuda_recalculada + cargos

if pago>deuda:
    print("\nusuario con tarjeta: {}".format(n_tarjeta))
    print("No se puede realizar un pago mayor al total de la deuda pasada")
else:
    print("\nusuario con tarjeta: {}".format(n_tarjeta))
    print("Pago: {}".format(pago))
    print("Interes mensual: {}".format(interes_mensual))
    print("Su nueva deuda: {}".format(nueva_deuda))
