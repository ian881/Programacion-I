

ARCHIVO_JUGADORES = "inscriptos.txt"
ARCHIVO_PAREJAS = "parejas.txt"


def leer_entero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            return int(texto)
        except ValueError:
            print("Ingrese un numero entero.")


def normalizar_categoria(texto):
    limpio = texto.strip().lower().replace(" ", "")
    if limpio in ("4", "4ta", "4ª", "4a"):
        return "4ta"
    if limpio in ("5", "5ta", "5ª", "5a"):
        return "5ta"
    if limpio in ("6", "6ta", "6ª", "6a"):
        return "6ta"
    return None


def buscar_jugador(jugadores, nombre):
    encontrado = None
    for jugador in jugadores:
        if jugador["nombre"].lower() == nombre.lower():
            encontrado = jugador
            break
    return encontrado


def jugador_ya_tiene_pareja(parejas, nombre):
    for pareja in parejas:
        if pareja["jugador1"].lower() == nombre.lower():
            return True
        if pareja["jugador2"].lower() == nombre.lower():
            return True
    return False


def cargar_jugadores():
    jugadores = []
    try:
        archivo = open(ARCHIVO_JUGADORES, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split("|")
            if len(partes) == 2:
                jugadores.append({"nombre": partes[0], "categoria": partes[1]})
        archivo.close()
    except FileNotFoundError:
        print("Todavia no hay inscriptos guardados. Se empieza una lista nueva.")
    return jugadores


def guardar_jugadores(jugadores):
    archivo = open(ARCHIVO_JUGADORES, "w", encoding="utf-8")
    for jugador in jugadores:
        archivo.write(jugador["nombre"] + "|" + jugador["categoria"] + "\n")
    archivo.close()


def cargar_parejas():
    parejas = []
    try:
        archivo = open(ARCHIVO_PAREJAS, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split("|")
            if len(partes) == 3:
                parejas.append({
                    "nombre": partes[0],
                    "jugador1": partes[1],
                    "jugador2": partes[2],
                })
        archivo.close()
    except FileNotFoundError:
        pass
    return parejas


def guardar_parejas(parejas):
    archivo = open(ARCHIVO_PAREJAS, "w", encoding="utf-8")
    for pareja in parejas:
        archivo.write(pareja["nombre"] + "|" + pareja["jugador1"] + "|" + pareja["jugador2"] + "\n")
    archivo.close()


def agregar_jugador(jugadores):
    nombre = input("Nombre del jugador: ").strip()
    while nombre == "" or buscar_jugador(jugadores, nombre) is not None:
        print("El nombre esta vacio o ya esta inscripto.")
        nombre = input("Nombre del jugador: ").strip()
    categoria = normalizar_categoria(input("Categoria (4ta, 5ta o 6ta): "))
    while categoria is None:
        print("La categoria tiene que ser 4ta, 5ta o 6ta.")
        categoria = normalizar_categoria(input("Categoria (4ta, 5ta o 6ta): "))
    jugadores.append({"nombre": nombre, "categoria": categoria})
    guardar_jugadores(jugadores)
    print(nombre, "quedo inscripto en categoria", categoria)


def mostrar_lista(jugadores):
    print("")
    if len(jugadores) == 0:
        print("No hay jugadores inscriptos.")
    else:
        print("Lista completa de inscriptos:")
        for i in range(len(jugadores)):
            jugador = jugadores[i]
            print(i + 1, "-", jugador["nombre"], "- categoria", jugador["categoria"])
    print("")


def consultar_jugador(jugadores):
    nombre = input("Nombre a buscar: ").strip()
    jugador = buscar_jugador(jugadores, nombre)
    print("")
    if jugador is None:
        print(nombre, "no esta inscripto.")
    else:
        print(jugador["nombre"], "esta inscripto.")
        print("Categoria:", jugador["categoria"])
    print("")


def sacar_jugador(jugadores, parejas):
    nombre = input("Nombre del jugador lesionado: ").strip()
    jugador = buscar_jugador(jugadores, nombre)
    if jugador is None:
        print("Ese jugador no esta en la lista.")
        return
    jugadores.remove(jugador)
    parejas_que_quedan = []
    for pareja in parejas:
        participa = pareja["jugador1"].lower() == jugador["nombre"].lower()
        participa = participa or pareja["jugador2"].lower() == jugador["nombre"].lower()
        if participa:
            print("Se elimino la pareja", pareja["nombre"], "porque le faltaba un jugador.")
        else:
            parejas_que_quedan.append(pareja)
    parejas.clear()
    for pareja in parejas_que_quedan:
        parejas.append(pareja)
    guardar_jugadores(jugadores)
    guardar_parejas(parejas)
    print(jugador["nombre"], "fue sacado de la lista.")


def armar_pareja(jugadores, parejas):
    if len(jugadores) < 2:
        print("Hacen falta al menos 2 jugadores inscriptos.")
        return
    nombre_pareja = input("Nombre de la pareja: ").strip()
    while nombre_pareja == "":
        print("La pareja tiene que tener un nombre.")
        nombre_pareja = input("Nombre de la pareja: ").strip()
    mostrar_lista(jugadores)
    nombre1 = input("Primer jugador: ").strip()
    nombre2 = input("Segundo jugador: ").strip()
    jugador1 = buscar_jugador(jugadores, nombre1)
    jugador2 = buscar_jugador(jugadores, nombre2)
    if jugador1 is None or jugador2 is None:
        print("Los dos jugadores tienen que estar inscriptos.")
        return
    if jugador1["nombre"].lower() == jugador2["nombre"].lower():
        print("Una pareja no puede tener dos veces al mismo jugador.")
        return
    if jugador_ya_tiene_pareja(parejas, jugador1["nombre"]) or jugador_ya_tiene_pareja(parejas, jugador2["nombre"]):
        print("Uno de esos jugadores ya esta en otra pareja.")
        return
    parejas.append({
        "nombre": nombre_pareja,
        "jugador1": jugador1["nombre"],
        "jugador2": jugador2["nombre"],
    })
    guardar_parejas(parejas)
    print("Pareja guardada:", nombre_pareja)


def mostrar_parejas(parejas):
    print("")
    if len(parejas) == 0:
        print("Todavia no hay parejas.")
    else:
        print("Parejas del torneo:")
        for pareja in parejas:
            print("-", pareja["nombre"] + ":", pareja["jugador1"], "y", pareja["jugador2"])
    print("")


def main():
    print("Torneo de padel - datos guardados en archivo")
    jugadores = cargar_jugadores()
    parejas = cargar_parejas()
    while True:
        print("1. Agregar un inscripto")
        print("2. Mostrar la lista completa")
        print("3. Buscar un jugador")
        print("4. Sacar un jugador lesionado")
        print("5. Armar una pareja")
        print("6. Ver parejas")
        print("7. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            agregar_jugador(jugadores)
        elif opcion == "2":
            mostrar_lista(jugadores)
        elif opcion == "3":
            consultar_jugador(jugadores)
        elif opcion == "4":
            sacar_jugador(jugadores, parejas)
        elif opcion == "5":
            armar_pareja(jugadores, parejas)
        elif opcion == "6":
            mostrar_parejas(parejas)
        elif opcion == "7":
            guardar_jugadores(jugadores)
            guardar_parejas(parejas)
            print("Datos guardados. Se puede cerrar el programa.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
