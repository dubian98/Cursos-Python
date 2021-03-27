#polimorfismo

class coche():
    def desplazamiento(self):
        print("me desplazo usando 4 ruedas")
class moto():
    def desplazamiento(self):
        print("mes desplazo usando 2 ruedas")

class camion():
    def desplazamiento(self):
        print("me desplazo usando 6 ruedas")


#mivehiculo=moto()
#mivehiculo.desplazamiento()

#micoche=coche()
#micoche.desplazamiento()

#micamion=camion()
#micamion.desplazamiento()
def DesplazamientoVehivulo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=coche()
DesplazamientoVehivulo(miVehiculo)

round(10.3456, 2)
print("h