#--------factores primos
def factors(num):
    output_list=[1]
    for i in range(2,num+1):
        while num%i == 0:
            output_list.append(i)
            num=num/i
    return(output_list)
factors(42)

#------------factores normales
def factors(num):
    output_list=[]
    for i in range(1,num):
        if num%i == 0:
            output_list.append(i)

    return(len(output_list))
factors(28)

