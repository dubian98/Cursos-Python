# clase
class coche():
    def __init__(self):
        self.__largochasis=250
        self.__anchochasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"
        
    
    def estado(self):
        print("el coche tiene ", self.__ruedas," ruedas. una ancho de ",self.__anchochasis," y un largo de ",self.__largochasis)



micoche=coche()

print(micoche.arrancar(True))
micoche.estado()

print("---------  --A continuacion creamos el segundo objeto ")


micoche2=coche()
print(micoche2.arrancar(False))
micoche2.__ruedas=5
micoche2.estado()
