from G3Ejercicio6 import Punto, Matematica

class Segmento:
    def __init__(self, punto1: Punto, punto2: Punto):
        self.punto1: Punto = punto1
        self.punto2: Punto = punto2

    def pitagoras(self):
        x_final = self.punto1.get_eje_x() - self.punto2.get_eje_x()
        y_final = self.punto1.get_eje_y() - self.punto2.get_eje_y()
        modulo = Matematica.pitagoras(x_final,y_final)
        modulo = round(modulo,2)
        return modulo

    def get_punto1(self):
        return self.punto1

    def get_punto2(self):
        return self.punto2

    def set_punto1(self, punto1):
        self.punto1 = punto1

    def set_punto2(self, punto2):
        self.punto2 = punto2

    def __str__(self):
        return "El modulo del segmento es : {}".format(self.pitagoras())

segmento_ej = Segmento(Punto(7,5),Punto(1,4))
print(segmento_ej)


