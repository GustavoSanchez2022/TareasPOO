class Alumno:
    def __init__(self,nombre,apellido,legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.notas = []

    def subir_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        suma = 0
        for i in range(len(self.notas)):
            suma += self.notas[i]
        promedio = suma/len(self.notas)
        return promedio

    def borrar_nota(self):
        self.notas.pop()

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def __str__(self):
        return "Alumno: {} {} \n" \
               "Legajo: {} \n" \
               "Notas: {} ".format(self.nombre,self.apellido,
                                   self.legajo,self.notas)

alumno_nuevo = Alumno("Gustavo","Sanchez",1234567)
alumno_nuevo.subir_nota(5)
alumno_nuevo.subir_nota(10)
alumno_nuevo.subir_nota(7)
print(alumno_nuevo)
print("Promedio es: {}".format(alumno_nuevo.promedio()))

alumno_nuevo.borrar_nota()
print(alumno_nuevo)