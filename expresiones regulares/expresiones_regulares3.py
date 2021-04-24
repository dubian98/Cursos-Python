#--------ragos--------
import re

lista_nombre=['ana',
                'pedro',
                'maria',
                'rosa',
                'sandra',
                'celia']

#--------los que comienzan-----
for elemento in lista_nombre:
    if re.findall("^[o-t]", elemento):
        print(elemento)

#-------los que no lo tenga
for elemento in lista_nombre:
    if re.findall("[^o-t]", elemento):
        print(elemento)
        