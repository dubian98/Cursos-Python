#---------ejemplo sencillo---------
"""def numero_par(num):
    if num % 2==0:
        return True"""

numeros=[17,24,7,39,8,51,92]
print(list(filter(lambda numero_par:numero_par%2==0,numeros)))


#-----filtro para una lista de objetos-------


class empleados:

    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de  {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[

empleados("juan","directos",75000),
empleados("ana","Presidente",85000),
empleados("antonio","administrativo",25000),
empleados("sara","Secretaria",27000),
empleados("mario","Botones",21000),

]

salarios_altos=filter(lambda empleados:empleados.salario>50000,listaEmpleados)

for empleadoSalario in salarios_altos:
    print(empleadoSalario)