# clase
class coche():
    largochasis=250
    anchochasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"
micoche=coche()

print(micoche.largochasis)
print("el coche tiene ", micoche.ruedas," ruedas")

#micoche.arrancar()
print(micoche.estado())