# crear un fichero

import pickle

lista_nombres = ["pedro","ana","maria","isabel"]

fichero_binario =open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del fichero_binario

#abrir un fichero 

import pickle 
fichero = open("lista_nombres", "rb")
lista=pickle.load(fichero)
print(lista)
x|