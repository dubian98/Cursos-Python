#crear excepcione

def evalua_edad(edad):
    if edad<0:
        raise TypeError("las edades no pueden ser negativas")
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"         
    elif edad < 65:
        return "eres maduro"
    elif edad < 100:
        return "cuidate"

print(evalua_edad(50))


#calcular razi cuandrada

import math

def calcula_raiz(num1):
    if num1<0:
        raise ValueError("el numero no puede ser negativo ")
    else:
        return math.sqrt(num1)

op1=(int(input("introduce un numero: ")))
try:

    print(calcula_raiz(op1))
except ValueError as Errornumeronegativo:
    print(Errornumeronegativo)

print("programa terminado")