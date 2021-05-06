def sum_pos_divisor(num):
    sum=0
    for i in range(1,num):
        if num%i == 0:
            sum+=i
    if sum==num:
        n=True
    else:
        n=False
    return n
sum_pos_sivisor(28)