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

