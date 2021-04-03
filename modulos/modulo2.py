#herencia 
class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arranca(self):
        self.enmarcha=True

    def acelera(self):
        self.acelera=True

    def frena(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEnmarcha: ",self.enmarcha,"\nAcelerea: ",self.acelera,"\nFrena: ",self.frena )

class furgoneta(vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"

class moto (vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="voy haciendo caballito"

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEnmarcha: ",self.enmarcha,"\nAcelerea: ",self.acelera,"\nFrena: ",self.frena,"\n", self.hcaballito )

class Velectrico(vehiculos):
    def __init__(self,marcaE,modeloE):
        super().__init__(marcaE,modeloE)
        self.autonimia=100
    cargando=False
    def cargaenergia(self):
        self.cargando=True
    def estado(self):
        super().estado()
        print("Cargando: ", self.cargando ,"\nAutonomia: ",self.autonimia)

