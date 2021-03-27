# funsion super()
class personas():
    def __init__ (self, nombre, edad, lrecidencia):
        self.nombre=nombre
        self.edad=edad
        self.lrecidencia=lrecidencia

    def descripcion(self):
        print("nombre: ",self.nombre,"\nEdad: ",self.edad,"\nLugar de recidencia: ",self.lrecidencia)

class empleado(personas):
    def __init__(self, salario, antiguedad,nombre_empleado,edad_empleado,recidencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,recidencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("salario: ",self.salario,"\nAntiguedad: ",self.antiguedad)
Dubian=personas("Dubian",23,"Colombia")
Dubian.descripcion()

javier=empleado(1500, 10,"gabriel",40,"colombia")
javier.descripcion()

print(isinstance(Dubian, empleado))
print(isinstance(javier,personas))