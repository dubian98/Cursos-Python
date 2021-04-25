def  funcion_decoradora(funcion_parametro):
    
    #*args ----> para poder que se reciba un numero indeterminado de parametros
    #**kwargs-----> adicionar argumentos con clave
    def funcion_interior(*args,**kwargs):
        #acciones adicionales que decoran
        print("vamos a realizar un calculo")
        funcion_parametro(*args,**kwargs)
        #acciones adicionales que decoran
        print("se ha terminado la ejecucion")
    return funcion_interior

@funcion_decoradora
def suma(a,b,c):
    print(a+b+c)

@funcion_decoradora
def resta(a,b):
    print(a-b)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))


suma(7,5,10)
resta(12,10)
potencia(exponente=3,base=5)