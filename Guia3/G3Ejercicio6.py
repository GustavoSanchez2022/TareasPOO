import math

class Matematica:
    @staticmethod
    def pitagoras(x,y):
        return math.sqrt(x**2+y**2)

class Punto:
    def __init__(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y

    def get_eje_x(self):
        return self.eje_x

    def get_eje_y(self):
        return self.eje_y

    def set_eje_y(self, eje_y):
         self.eje_y = eje_y

    def set_eje_x(self, eje_x):
        self.eje_x = eje_x

    def cuadrante(self, x, y):
        if (x*y) > 0:
            if x>0:
                nroCuadrante = 1
            else:
                nroCuadrante = 3
        else:
            if x<0:
                nroCuadrante = 2
            else:
                nroCuadrante = 4

        return nroCuadrante

    def pitagoras(self):
        modulo = Matematica.pitagoras(self.eje_x,self.eje_y)
        modulo = round(modulo,2)
        return modulo

    def __str__(self):
        return "El numero de cuadrante de los puntos ({};{}) es el: {}\n" \
               "Y el modulo es {}".format(self.eje_x, self.eje_y,
                self.cuadrante(self.eje_x,self.eje_y),self.pitagoras())
"""
PuntoEjemplo = Punto(4,2)
print(PuntoEjemplo)"""