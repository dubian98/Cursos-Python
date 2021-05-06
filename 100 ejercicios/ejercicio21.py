def Fibonacci():
    import random
    n=random.randint(5,11)
    secuencia_salida=[0,1]
    for i in range(2,n) :
        x1=secuencia_salida[len(secuencia_salida)-1]+secuencia_salida[len(secuencia_salida)-2]
        secuencia_salida.append(x1)
    x2=n
    return  n,secuencia_salida

Fibonacci()


forma 2
def Fibonacci(n):
    secuencia_salida=[0,1]
    a=0
    b=1
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        secuencia_salida.append(c)
    return n,secuencia_salida
        
Fibonacci(6)

