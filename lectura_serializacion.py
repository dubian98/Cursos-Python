
import pickle
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


fichero2 = open("loscoches","rb")
miscoches=pickle.load(fichero2)
fichero2.close()

for c in miscoches:
    print(c.estado())