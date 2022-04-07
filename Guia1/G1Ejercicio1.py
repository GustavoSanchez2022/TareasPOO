def Multiplico(a,b):
    return a*b

def UltimoNum(a):
    ultimo = a % 10
    return ultimo

def Comparar(x,y):
    return  UltimoNum(x) == UltimoNum(y)

def Ejercicio(a,b,c):
    multiplo = Multiplico(a,b)
    return Comparar(multiplo,c)

"""print(Ejercicio(25,21,125))"""
