import random
def sum_digits():
    n=random.randint(100,300)
    s=0
    for i in str(n):
        a=int(i)
        s+=a
    return s,n
sum_digits()