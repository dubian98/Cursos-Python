# excepciones 2
def divide():
    try:
        op1=(float(input("introduce el primer numero: ")))
        op2=(float(input("introduce el segundo numero: ")))

        print("la divivion es: ",op1/op2)
    except ValueError:
        print("el valor no es correcto ")
    except ZeroDivisionError:
        print("no se puede dividir entre cero ")
    finally: 
        print("calculo finalizados")
divide()

#solo finally

def divide():
    try:
        op1=(float(input("introduce el primer numero: ")))
        op2=(float(input("introduce el segundo numero: ")))

        print("la divivion es: ",op1/op2)

    finally: 
        print("calculo finalizados")
divide()
