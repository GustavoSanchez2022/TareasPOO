class Fecha:
    def __init__(self,dia , mes , anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def dia_siguiente(self):
        dia_sgte = self.dia + 1
        return dia_sgte

    def dia_anterior(self):
        return self.dia - 1

    def canti(self, dia_new):
        diferencia = dia_new - self.dia
        return diferencia

    def get_dia(self):
        return self.dia

    def get_mes(self):
        return self.mes

    def get_anio(self):
        return self.anio

    def set_dia(self, dia):
        self.dia = dia

    def set_mes(self, mes):
        self.mes = mes

    def set_anio(self, anio):
        self.anio = anio

    def __str__(self):
        return "La fecha es {}/{}/{} \n" \
               "Y su diferencia entre la fecha nueva es: {}".format(
            self.dia,self.mes,self.anio,self.canti(20)
        )

fecha_hoy = Fecha(25,10,2022)
print(fecha_hoy)