from calculadora.tarjeta import Tarjeta

def advertencia(func):
        def wrapper(ref):
            print("ADVERTANCIA!! Solo pagos Totales")
            func(ref)
        return wrapper

class Tarjeta_Servicios(Tarjeta):
        

    def crea_tarjeta(self):
        """Función para crear una tarjeta nueva"""
        try:
            n_tarjeta=input("Inserte su nombre de tarjeta: ")
            deuda=int(input("Ingrese su deuda actual: "))
            pago=int(input("Inserte el pago que desea realizar: "))
            cargos=int(input("Ingrese los nuevos cargos a su tarjeta: "))

            if pago>deuda:
                print("\nusuario con tarjeta: {}".format(n_tarjeta))
                print("No se puede realizar un pago mayor al total de la deuda pasada")
            else:
                self.datos["num_tarjeta"]=n_tarjeta
                self.datos["deuda"]=deuda
                self.datos["pago"]=pago
                self.datos["cargos"]=cargos

            return self.datos
        except TypeError:
            print("No se metio el valor adecuado")


    def captura_nueva_deuda(self):
        """Función para capturar una nueva deuda"""

        deuda_recalculada = (self.datos["deuda"]-self.datos["pago"])
        self.datos["nueva_deuda"]= deuda_recalculada + self.datos["cargos"]

        return self.datos

    @advertencia
    def pago_recurrente(self):
        """Función que realiza un mismo pago hasta que la deuda vuelva a 0"""

        mes = 1
        while self.datos["deuda"]>0:
            print(mes)
            self.generar_reporte()
            self.datos["deuda"] = (self.datos["deuda"]-self.datos["pago"])
            mes+=1

    @advertencia
    def pagos_diferentes(self):
        """Función que deposita diferentes pagos programados por el numero de meses seleccionados"""

        pagos_meses=[]
        meses=int(input("Insertar el número de meses que deseas pagar automáticamente: "))
        print("Insertar los pagos a continuación: ")
        for i in range(meses):
            pagos_meses.append(int(input("{} : ".format(i+1))))
        for pago in pagos_meses:
            self.datos["pago"] = pago
            self.generar_reporte()
    
