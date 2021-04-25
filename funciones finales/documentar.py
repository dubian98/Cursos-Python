class areas:

    def areacuadrado(lado):
        """calcula el area de un cuadrado elevando el lado del cuadrado en un triangulo"""
        return "el area del cuadrado es: " + str(lado*lado)

    def areatriangulo(base,altura):
        """calcula el area de un triangulo"""
        return "el area del triangulo es: " + str(base*altura/2)

"""print(areacuadrado(10))
print(areatriangulo(5,25))
print(areacuadrado.__doc__)    """

#help(areas.areatriangulo)
help(areas)