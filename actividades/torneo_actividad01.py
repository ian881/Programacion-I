# Gestion de torneo - Actividad 01
# Carga jugadores en un vector y arma parejas de exactamente 2.


def leer_entero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            numero = int(texto)
            return numero
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
    cantidad = leer_entero("Cuantos jugadores van a participar en el torneo? ")
    while cantidad < 2:
        print("Para armar parejas tienen que ser al menos 2.")
        cantidad = leer_entero("Cuantos jugadores van a participar en el torneo? ")
    for i in range(cantidad):
        print("")
        print("Jugador", i + 1)
        nombre = input("Nombre: ").strip()
        while nombre == "" or buscar_jugador(jugadores, nombre) is not None:
            print("El nombre esta vacio o ya fue inscripto.")
            nombre = input("Nombre: ").strip()
        categoria = normalizar_categoria(input("Categoria (4ta, 5ta o 6ta): "))
        while categoria is None:
            print("La categoria tiene que ser 4ta, 5ta o 6ta.")
            categoria = normalizar_categoria(input("Categoria (4ta, 5ta o 6ta): "))
        jugadores.append({"nombre": nombre, "categoria": categoria})
    return jugadores


def mostrar_jugadores(jugadores):
    print("")
    print("Jugadores inscriptos:")
    for i in range(len(jugadores)):
        jugador = jugadores[i]
        print(i + 1, "-", jugador["nombre"], "- categoria", jugador["categoria"])
    print("")


def armar_pareja(jugadores, parejas):
    print("")
    nombre_pareja = input("Nombre de la pareja: ").strip()
    while nombre_pareja == "":
        print("La pareja tiene que tener un nombre.")
        nombre_pareja = input("Nombre de la pareja: ").strip()
    mostrar_jugadores(jugadores)
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
    print("Pareja armada:", nombre_pareja)
    print(jugador1["nombre"], "y", jugador2["nombre"])


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
    print("Inscripcion del torneo de padel")
    jugadores = cargar_jugadores()
    parejas = []
    mostrar_jugadores(jugadores)
    while True:
        print("1. Armar una pareja")
        print("2. Ver jugadores")
        print("3. Ver parejas")
        print("4. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            armar_pareja(jugadores, parejas)
        elif opcion == "2":
            mostrar_jugadores(jugadores)
        elif opcion == "3":
            mostrar_parejas(parejas)
        elif opcion == "4":
            mostrar_parejas(parejas)
            print("Fin del programa. Estos datos se pierden al cerrar.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
