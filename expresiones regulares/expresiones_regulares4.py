import re

nombre1="Sandra lopez"
nombre2="Antonio gomez"
nombre3="landra lopez"


if re.match("Sandra",nombre2):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

#--------si queremos ignorar el keysensitive----

if re.match("Sandra",nombre3,re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

#----comodin punto-----
if re.match(".andra",nombre3):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

# buscar si se quirer patrones de busqueda en python para ver mas expresiones regulares

#codenas de texto que empiecen por numero 
import re

nombre1="Sandra lopez"
nombre2="455345345"
nombre3="a4534534534"

if re.match("\d",nombre2):
    print("Hemos encontrado el numero")
else:
    print("No hemos encontrado el numero")


#--------funsion search--------

import re

nombre1="Sandra lopez"
nombre2="Antonio gomez"
nombre3="landra lopez"


if re.search("lopez",nombre1):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")
