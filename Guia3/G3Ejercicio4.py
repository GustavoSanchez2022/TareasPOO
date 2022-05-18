def alumno():
    listaAlumno = []
    nombre = input("Nombre de Alumno: ")
    apellido = input("Apellido de Alumno: ")
    Legajo = int(input("Legajo de alumno: "))
    notas = notas_estudiantes()
    promedio = calcular_promedio(notas)
    listaAlumno.append(nombre)
    listaAlumno.append(apellido)
    listaAlumno.append(Legajo)
    listaAlumno.append(notas)
    listaAlumno.append(promedio)
    return listaAlumno

def notas_estudiantes():
    listaDeNotas = []
    respuesta = True
    while respuesta:
        valor = input("¿Quiere agregar notas al estudiante? SI/NO").upper()
        if valor == "NO":
            respuesta = False
        else:
            nota = int(input("Nota para subir: "))
            listaDeNotas.append(nota)

    return listaDeNotas

def calcular_promedio(listaDeNotas):
    suma = 0
    for i in listaDeNotas:
        suma = suma + i
    promedio = float(suma/len(listaDeNotas))
    return promedio

print("Promedio del Alumno es: {}".format(alumno()[-1]))

"""notas = []
notas = notas_estudiantes(notas)
print(notas)
print("Promedio es de {}".format(calcular_promedio(notas)))"""
