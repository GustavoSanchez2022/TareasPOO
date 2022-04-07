"""Convertir un numero binario a decimal"""
def calcularDicimal(binario):
    binario = binario[::-1]
    posicion = 0
    contador = 0
    for i in binario:
        contador = contador + int(i)*(2**posicion)
        posicion += 1

    return contador

#print(calcularDicimal([1,1,1,1]))

