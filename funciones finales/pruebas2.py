import math

def raizcuadrada(listanumeros):
    """
    la función devuelve una lista con las raiz cuadrada de los elemento numericos pasado spor parámetros en otra lista
    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizcuadrada(lista)
    [2.0, 3.0, 4.0]
    >>> lista=[]
    >>> for i in [4,-9,16]:
    ...     lista.append(i)
    >>> raizcuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """

    return [math.sqrt(n) for n in listanumeros]

#print (raizcuadrada([9,-16,25,36]))
import doctest
doctest.testmod()