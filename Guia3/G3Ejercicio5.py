class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area_rectangulo(self):
        area = self.base * self.altura
        return area

    def perimetro_rectangulo(self):
        perimetro = 2*(int(self.base+self.altura))
        return perimetro

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def __str__(self):
        return "Altura es {} y base {}. \n" \
               "Perimetro: {}\n" \
               "Area: {} \n".format(self.altura,self.base,self.perimetro_rectangulo(),self.area_rectangulo())