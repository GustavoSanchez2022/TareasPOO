def tableroDeAjedrez():
    list = []
    for i in range (8):
        list.append([0]*8)#INICIALIZO LA MATRIZ
    for i in range(8):
        for j in range(8):
            if ((i+j)%2==0):
                list[i][j] = "black"
            else:
                list[i][j] = "white"
    if (i+j) == 0:
        list[i][j] = "black"

    return list

def colorPosicion(posicion):
    tablero = tableroDeAjedrez()
    filas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    columnas = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for i in range(8):
        if (posicion[0] == filas[i]):
            indiceLetra = i
    for j in range(8):
        if (posicion[1] == columnas[j]):
            indiceNum = j

    valor_de_la_matriz = tablero[indiceLetra][indiceNum]

    return valor_de_la_matriz

#print(colorPosicion("a1"))
