from datetime import datetime
def check_friday_13(yr,mon):
    day=13
    if datetime(yr,mon,day).weekday()==4:
        v13=True
    else:
        v13=False
    return (yr,mon,day),v13
check_friday_13(1998,10)