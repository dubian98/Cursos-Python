import pickle
class persona:
    def __init__(self, nombre, genero,edad):
        self.nombre = nombre
        self.genero= genero
        self.edad=edad
        print("se a creado a una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class lista_personas:
    personas=[]
    def __init__(self):
        listaDePersonas=open("fichero_externo","ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("el fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)
    def agregar_personas(self,p):
        self.personas.append(p)
    def  mostrar_personas(self):
        for p in self.personas:
            print(p)

    def guardarpersonasenficheroexterno(self):
        lista_personas=open("fichero_externo","wb")
        pickle.dump(self.personas,lisDePersonas)
        listasDePersonas.close()
        del(listaDePersonas)
    def mostrarinformacionficheroexterno(self):
        print("la informacion del fichero externo es la siguiente")
        for p in self.personas:
            print(p)

milista=lista_personas()
p=persona("rodrigo","masculino","29")
milista.agregar_personas(p)
milista.mostrarinformacionficheroexterno()

p=persona("antonio","masculino","29")
milista.agregar_personas(p)

p=persona("ana","femenino","29")
milista.agregar_personas(p)

milista.mostrar_personas()