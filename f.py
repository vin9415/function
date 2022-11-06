#keyword variable length argument

def details(name, **data):
    print(name)

    for i , j in data.items():
        print(i,j)


details("vinit" ,place="ballia",no="8840025527")

a=15 #global

def fun():
    a=5 #local
    print(a)


    fun()
    print(a)