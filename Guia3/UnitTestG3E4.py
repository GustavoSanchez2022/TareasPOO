import unittest
from G3EjercicioOBJETO import Alumno

class MyTestCase(unittest.TestCase):

    def comparar(self, lista, listaNotas):
        if (len(lista) == len(listaNotas)):
            for i in range(len(lista)):
                if lista[i] == listaNotas[i]:
                    valor = True
                else:
                    valor = False
        return valor

    def test_something(self):
        estudiante = Alumno("Karim", "Benzema", 9999999)
        estudiante.subir_nota(7)
        estudiante.subir_nota(6)
        self.assertEqual(estudiante.promedio(), 6.5)  # add assertion here

    def test_something2(self):
        estudiante = Alumno("Karim", "Benzema", 9999999)
        estudiante.subir_nota(7)
        estudiante.subir_nota(6)
        listaAux = [7,6]
        self.assertTrue(self.comparar(estudiante.notas,listaAux))

if __name__ == '__main__':
    unittest.main()
