class Calculadora:
    def __init__(self, marca, memoria, rango, modelo):
        self.marca = marca
        self.memoria = memoria
        self.rango = rango
        self.modelo = modelo

    def set_rango(self):
        self.rango = 10000

    def sumar(self, num1, num2):
        suma = num1 + num2
        if suma < self.rango:
            return suma
        else:
            print("Error: fuera de rango")
            suma = "null"
            return suma

    def restar(self, num1, num2):
        resta = num1 - num2
        return resta

    def multiplicacion(self, num1, num2):
        multiplicacion = num1 * num2
        return multiplicacion

    def division(self, num1, num2):
        dividir = num1 / num2
        return dividir

    def factorial(self,num1):
        multiploFactorial = 1
        for i in range(1,num1):
            multiploFactorial = multiploFactorial*(i+1)

        return multiploFactorial


    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def __str__(self):
        return "Datos de Calculadora \n" \
               "Marca: {}\n" \
               "Modelo: {}\n" \
               "Ultimo resultado:{}\n".format(self.marca, self.modelo, self.memoria)

"""calculadora_nueva = Calculadora("Casio", "NULL", 1000000, "fx550")
print(calculadora_nueva.factorial(4))"""

"""
calculadora_nueva.sumar(2,4)
print(calculadora_nueva)"""
