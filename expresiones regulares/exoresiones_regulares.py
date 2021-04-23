import re 
cadena = "vamos a aprender expresiones regulares en python. python es un lenguaje"
#print(re.search("aprender",cadena))

textobuscar="python"
"""if re.search(textobuscar,cadena) is not None:
    print("he encontrado el texto")
else:
    print("no he encontrado el texto")"""


textoencontrado = re.search(textobuscar,cadena)

print(textoencontrado.start())
print(textoencontrado.end())
print(textoencontrado.span())

# metodo, findall

print(len(re.findall(textobuscar,cadena)))