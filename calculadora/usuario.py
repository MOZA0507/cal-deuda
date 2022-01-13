import csv

class Usuario():
    def __init__(self, name, tarjetas):
        self.name = name
        self.tarjetas = tarjetas

    def __str__(self):
        cadena = "Usuario: {} cuenta con un total de {} tarjetas".format(self.name,len(self.tarjetas))
        return cadena

    def añadir_tarjetas(self):
        num=int(input("Numero de tarjetas a añadir: "))
        print("Añadir tarjetas a continuación")
        for i in range(num):
            self.tarjetas.append(input("{}: ".format(i+1)))
        return self.tarjetas

    def lista_tarjetas(self):
        """Función que imprime datos de diferentes tarjetas"""
        print("Tarjetas del usuari@: {}".format(self.name))
        i=1
        for tarjeta in self.tarjetas:
            print("{}: {}".format(i,tarjeta))
            i+=1

    def crear_csv(self):
        header = []
        header.append(self.name)
        with  open("usuario.csv",'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(self.tarjetas)
