from lib import getvalue
no1=int(getvalue("No1"))
no2=int(getvalue("No2"))
no3=int(getvalue("No3"))

if no1>0 and no2>0 and no3>0 :
    if no1>no2 and no1>no3:
        print(no1," is a maximum no")
    elif no2>no3:
        print(no2," is a maximum no")
    else :
        print(no3," is a maximum no")
else :
    if no1<0:
        print(no1," is invalid")
    elif no2<0:
        print(no2," is invalid")
    else:
        print(no3," is invalid")

