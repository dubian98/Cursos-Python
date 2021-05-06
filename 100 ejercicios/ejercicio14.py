def booleans(x,y,z):
    a=0
    b=0
    c=0
    if x==True:
        a=1
    if y==True:
        b=1        
    if z==True:
        c=1
    if (a+b+c)>=2:
        n=True
    else:
        n=False
    return (x,y,z,n)
booleans(True,True,False)  