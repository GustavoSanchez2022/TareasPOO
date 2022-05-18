import math

class Matematica:
    @staticmethod
    def pitagoras(x,y):
        return math.sqrt(x**2+y**2)


class Segmento:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def pitagoras(self):
        parteA = self.punto1[0] - self.punto2[0]
        parteB = self.punto1[1] - self.punto2[1]
        modulo = Matematica.pitagoras(parteA,parteB)
        modulo = round(modulo,2)
        return modulo

recta = Segmento([2,3],[3,5])
print(recta.pitagoras())