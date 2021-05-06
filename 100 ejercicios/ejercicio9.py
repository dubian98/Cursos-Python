def count_num_digits(string):
    count=0
    for i in string:
        try:
            int(i)
            count+=1
        except:
            count+=0
    return count
count_num_digits("asasas54456")
