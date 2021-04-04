# escritura
from io import open 

archivo_texto = open("archivo.txt","w")
frase = "estupendo dia para estudiar \n miercoles"

archivo_texto.write(frase)

archivo_texto.close()


# lectura

from io import open 

archivo_texto = open("archivo.txt","r")

texto = archivo_texto.read()
archivo_texto.close()
print("lo que dice en el archivo es \n",texto)

# leer lineas

from io import open 

archivo_texto = open("archivo.txt","r")

lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto[1])

#agregar texto
from io import open 

archivo_texto = open("archivo.txt","a")

archivo_texto.write("\nsiempre es una buena ocacion para estudiar python")
archivo_texto.close()

#punteros 
from io import open 

archivo_texto = open("archivo.txt","r+") #lectura y escritura

print(archivo_texto.read(11))

archivo_texto.seek(30)
archivo_texto.write("comienzo del texto\n")
print(archivo_texto.read())


#agregar una linea

from io import open 

archivo_texto = open("archivo.txt","r+") #lectura y escritura

lista_texto = archivo_texto.readlines()

lista_texto[2] = "333333333333\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)
archivo_texto.seek(0)
print(archivo_texto.read())

archivo_texto.close()