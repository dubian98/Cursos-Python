class empleados:

    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de  {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

empleados("juan","directos",6700),
empleados("ana","Presidente",7500),
empleados("antonio","administrativo",2100),
empleados("sara","Secretaria",2150),
empleados("mario","Botones",1800),

]

def calculo_comision(empleados):
    if empleados.salario <= 3000:

        empleados.salario=empleados.salario*1.03
    return empleados

lista_empleados=map(calculo_comision,listaEmpleados)

for empleado in lista_empleados:
    print(empleado)