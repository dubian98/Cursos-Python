#generadores
#1 función
def generapares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)

        num +=1
    return lista
generapares(10)


#generador

def generapares(limite):
    num=1
    
    while num<limite:
        yield num*2

        num +=1
devuelvepares=generapares(10)

for i in devuelvepares:
    print(i)


#imprimir unos cuantos
def generapares(limite):
    num=1
    
    while num<limite:
        yield num*2

        num +=1
devuelvepares=generapares(10)


print(next(devuelvepares))
print("mas codigo ...")

print(next(devuelvepares))
print("mas codigo ...")

print(next(devuelvepares))
print("mas codigo ...")
