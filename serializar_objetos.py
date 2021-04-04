#creacion
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


coche1=vehiculos("mazda","mx5")
coche2=vehiculos("renauld","logan")
coche3=vehiculos("ford","f-150")
coches=[coche1,coche2,coche3]


fichero=open("loscoches","wb")
pickle.dump(coches,fichero)
fichero.close()
del fichero

#lectura
import pickle
fichero2=open("loscoches","rb")
micoches=pickle.load(fichero2)
fichero2.close()

for i in micoches:
    print(c.estado())

print("hola")