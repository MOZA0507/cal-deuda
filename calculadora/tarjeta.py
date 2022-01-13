import csv
import json

class Tarjeta():

    def __init__(self,datos):
        self.datos=datos

    def crea_tarjeta(self):
        """Función para crear una tarjeta nueva"""
        n_tarjeta=input("Inserte su nombre de tarjeta: ")
        t_interes=int(input("Inserte tasa de interes: "))
        deuda=int(input("Ingrese su deuda actual: "))
        pago=int(input("Inserte el pago que desea realizar: "))
        cargos=int(input("Ingrese los nuevos cargos a su tarjeta: "))

        if pago>deuda:
            print("\nusuario con tarjeta: {}".format(n_tarjeta))
            print("No se puede realizar un pago mayor al total de la deuda pasada")
        else:
            self.datos["num_tarjeta"]=n_tarjeta
            self.datos["t_interes"]=t_interes
            self.datos["deuda"]=deuda
            self.datos["pago"]=pago
            self.datos["cargos"]=cargos

        return self.datos

    def captura_nueva_deuda(self):
        """Función para capturar una nueva deuda"""

        interes_mensual= self.datos["t_interes"]/12
        deuda_recalculada = (self.datos["deuda"]-self.datos["pago"])*(1+interes_mensual)
        self.datos["nueva_deuda"]= deuda_recalculada + self.datos["cargos"]

        return self.datos

    def generar_reporte(self):
        """Función que genera un reporte con los datos de un dict"""

        print("\n")
        for k,v in self.datos.items():
            print("{} : {}".format(k,v))


    def pago_recurrente(self):
        """Función que realiza un mismo pago hasta que la deuda vuelva a 0"""

        mes = 1
        while self.datos["deuda"]>0:
            print(mes)
            self.generar_reporte()
            self.datos["deuda"] = (self.datos["deuda"]-self.datos["pago"])
            mes+=1

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

    def crear_csv_tarjeta(self):
        with open("tarjeta.csv",'w') as f:
            writer = csv.writer(f)
            for k,v in self.datos.items():
                writer.writerow([k,v])
    
    def crear_json(self):
        json_object = json.dumps(self.datos,indent=4)
        with open("tarjeta.json",'w') as outfile:
            outfile.write(json_object)
    
    def json_a_dic(self):
        with open("tarjeta.json") as outfile:
            data = json.load(outfile)
            print(data)