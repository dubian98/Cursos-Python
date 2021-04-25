def  funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #acciones adicionales que decoran
        print("vamos a realizar un calculo")
        funcion_parametro()
        #acciones adicionales que decoran
        print("se ha terminado la ejecucion")
    return funcion_interior

@funcion_decoradora
def suma():
    print(12+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()