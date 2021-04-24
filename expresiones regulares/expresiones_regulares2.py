#----------meta caracteres----------------
#--------------------anclas

    import re

    lista_nombre=['ana gomez',
                    'mariaz martin',
                    'sandra lopez',
                    'santiago martin',
                    'sandra martinez']

    #--------los que comienzan-----
    """for elemento in lista_nombre:
        if re.findall("^sandra", elemento):
            print(elemento)"""
    #----------- los que finalizan en:-----------
    for elemento in lista_nombre:
        if re.findall("z", elemento):
            print(elemento)

#--------buscar un caracter en especifico----------
"""for elemento in lista_nombre:
    if re.findall("[g]", elemento):
        print(elemento)"""


#----- buscar diferentes palabras similares------
for elemento in lista_nombre:
    if re.findall("marti[nez]", elemento):
        print(elemento)