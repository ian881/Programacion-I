

PROMEDIO_MINIMO = 6
ASISTENCIA_MINIMA = 75

alumnos = [
    {"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90},
    {"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60},
    {"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95},
    {"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85},
]


def promedio(notas):
    suma = 0
    for nota in notas:
        suma = suma + nota
    return suma / len(notas)


def esta_regular(alumno):
    if len(alumno["notas"]) != 4:
        return False
    if promedio(alumno["notas"]) < PROMEDIO_MINIMO:
        return False
    if alumno["asistencia"] < ASISTENCIA_MINIMA:
        return False
    return True


def buscar_alumno(lista, nombre):
    encontrado = None
    for alumno in lista:
        if alumno["nombre"].lower() == nombre.lower():
            encontrado = alumno
            break
    return encontrado


def mostrar_alumno(alumno):
    nota_promedio = promedio(alumno["notas"])
    print("Alumno:", alumno["nombre"])
    print("Notas:", alumno["notas"])
    print("Promedio:", nota_promedio)
    print("Asistencia:", alumno["asistencia"], "%")
    if esta_regular(alumno):
        print("Estado: REGULAR")
    else:
        print("Estado: NO ESTA REGULAR")
        if nota_promedio < PROMEDIO_MINIMO:
            print("- el promedio no llega a", PROMEDIO_MINIMO)
        if alumno["asistencia"] < ASISTENCIA_MINIMA:
            print("- la asistencia no llega a", ASISTENCIA_MINIMA, "%")
    print("")


def mostrar_todos(lista):
    for alumno in lista:
        mostrar_alumno(alumno)


def main():
    print("Consulta de alumnos regulares")
    print("Promedio minimo:", PROMEDIO_MINIMO)
    print("Asistencia minima:", ASISTENCIA_MINIMA, "%")
    print("")
    while True:
        print("1. Ver todos los alumnos")
        print("2. Consultar un alumno")
        print("3. Salir")
        opcion = input("Opcion: ")
        print("")
        if opcion == "1":
            mostrar_todos(alumnos)
        elif opcion == "2":
            nombre = input("Nombre del alumno: ")
            alumno = buscar_alumno(alumnos, nombre)
            print("")
            if alumno is None:
                print("Ese alumno no esta en la lista.")
                print("")
            else:
                mostrar_alumno(alumno)
        elif opcion == "3":
            print("Fin del programa.")
            break
        else:
            print("Opcion no valida.")
            print("")


if __name__ == "__main__":
    main()
