# encapsulamiento
class coche():
    def __init__(self):
        self.__largochasis=250
        self.__anchochasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeointerno()

        if(self.__enmarcha and chequeo):
            return "el coche esta en marcha"

        elif(self.__enmarcha and chequeo == False):
            return "algo ha ido mal en el chequeo, no podemos arrancar"

        else:
            return "el coche esta parado"
        
    
    def estado(self):
        print("el coche tiene ", self.__ruedas," ruedas. una ancho de ",self.__anchochasis," y un largo de ",self.__largochasis)

    def __chequeointerno(self):
        print("se va a realizar un chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok"and self.puertas=="cerradas"):
            return True
        else:
            return False
        

micoche=coche()

print(micoche.arrancar(True))
micoche.estado()


print("---------  --A continuacion creamos el segundo objeto ")


micoche2=coche()
print(micoche2.arrancar(False))



micoche2.estado()

