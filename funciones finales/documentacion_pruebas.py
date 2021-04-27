# primer ejemplo
"""
def areatriangulo(base,altura):
    """
    calcula el área de un triangulo dado
    >>> areatriangulo(3,6)
    'el area del triagulo es: 9.0'

    >>> areatriangulo(4,5)
    'el area del triagulo es: 10.0'

    >>> areatriangulo(9,3)
    'el area del triagulo es: 13.5'
    """
    return "el area del triagulo es: " + str((base*altura)/2)
#se realiza la prueba
import doctest
doctest.testmod()
"""
def compruebamail(maiusuario):
    """ 
    la función comprueba mail evalúa un mail recibido en busca de la @.
    si tengo una @ es correcto, si tiene mas de una 
    @ es incorrecto, 
    si la arroba esta al final es incorrecto
    >>> compruebamail('juan@cursos.es')
    True
    >>> compruebamail('juancursos.es@')
    False
    >>> compruebamail('juancursos.es')
    False
    >>> compruebamail('juan@@cursos.es')
    False
    """
    arroba=maiusuario.count("@")
    if arroba!=1 or maiusuario.rfind("@")==(len(maiusuario)-1)or maiusuario.find("@")==0:
        return False
    else:
        return True


import doctest
doctest.testmod()