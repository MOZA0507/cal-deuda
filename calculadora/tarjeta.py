class Tarjeta():


    def crea_tarjeta(self):
        """Función para crear una tarjeta nueva"""

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

    def captura_nueva_deuda(self,tarjeta_data):
        """Función para capturar una nueva deuda"""

        interes_mensual= tarjeta_data["t_interes"]/12
        deuda_recalculada = (tarjeta_data["deuda"]-tarjeta_data["pago"])*(1+interes_mensual)
        tarjeta_data["nueva_deuda"]= deuda_recalculada + tarjeta_data["cargos"]

        return tarjeta_data

    def generar_reporte(self,tarjeta_data):
        """Función que genera un reporte con los datos de un dict"""

        print("\n")
        for k,v in tarjeta_data.items():
            print("{} : {}".format(k,v))


    def pago_recurrente(self,tarjeta_data):
        """Función que realiza un mismo pago hasta que la deuda vuelva a 0"""

        mes = 1
        while tarjeta_data["deuda"]>0:
            print(mes)
            self.generar_reporte(tarjeta_data)
            tarjeta_data["deuda"] = (tarjeta_data["deuda"]-tarjeta_data["pago"])
            mes+=1

    def pagos_diferentes(self,tarjeta_data):
        """Función que deposita diferentes pagos programados por el numero de meses seleccionados"""

        pagos_meses=[]
        meses=int(input("Insertar el número de meses que deseas pagar automáticamente: "))
        print("Insertar los pagos a continuación: ")
        for i in range(meses):
            pagos_meses.append(int(input("{} : ".format(i+1))))
        for pago in pagos_meses:
            tarjeta_data["pago"] = pago
            self.generar_reporte(tarjeta_data)