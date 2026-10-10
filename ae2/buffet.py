# Practica: El buffet de la Facultad
# El catalogo se guarda en productos.txt
# Las cantidades vendidas de cada dia se guardan en ventas.txt

ARCHIVO_PRODUCTOS = "productos.txt"
ARCHIVO_VENTAS = "ventas.txt"
DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes"]

CATALOGO_INICIAL = [
    {"codigo": 101, "nombre": "Cafe con leche", "precio": 1500},
    {"codigo": 102, "nombre": "Medialuna", "precio": 700},
    {"codigo": 103, "nombre": "Sandwich de miga", "precio": 1800},
    {"codigo": 104, "nombre": "Agua mineral 500 ml", "precio": 1000},
    {"codigo": 105, "nombre": "Empanada", "precio": 1200},
    {"codigo": 106, "nombre": "Chipa (100 g)", "precio": 1300},
]


def leer_entero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            return int(texto)
        except ValueError:
            print("Ingrese un numero entero.")


def buscar_producto(productos, codigo):
    encontrado = None
    for producto in productos:
        if producto["codigo"] == codigo:
            encontrado = producto
            break
    return encontrado


def unidades_producto(ventas, codigo):
    total = 0
    for cantidad in ventas[codigo]:
        total = total + cantidad
    return total


def recaudacion_dia(productos, ventas, dia):
    total = 0
    indice = dia - 1
    for producto in productos:
        cantidad = ventas[producto["codigo"]][indice]
        total = total + cantidad * producto["precio"]
    return total


def recaudacion_total(productos, ventas):
    total = 0
    for dia in range(1, 6):
        total = total + recaudacion_dia(productos, ventas, dia)
    return total


def productos_mas_vendidos(productos, ventas):
    mayor = 0
    for producto in productos:
        unidades = unidades_producto(ventas, producto["codigo"])
        if unidades > mayor:
            mayor = unidades
    if mayor == 0:
        return []
    ganadores = []
    for producto in productos:
        if unidades_producto(ventas, producto["codigo"]) == mayor:
            ganadores.append(producto)
    return ganadores


def dias_mayor_recaudacion(productos, ventas):
    if recaudacion_total(productos, ventas) == 0:
        return []
    mayor = 0
    for dia in range(1, 6):
        recaudacion = recaudacion_dia(productos, ventas, dia)
        if recaudacion > mayor:
            mayor = recaudacion
    ganadores = []
    for dia in range(1, 6):
        if recaudacion_dia(productos, ventas, dia) == mayor:
            ganadores.append(dia)
    return ganadores


def productos_sin_ventas(productos, ventas):
    sin_ventas = []
    for producto in productos:
        if unidades_producto(ventas, producto["codigo"]) == 0:
            sin_ventas.append(producto)
    return sin_ventas


def crear_ventas_vacias(productos):
    ventas = {}
    for producto in productos:
        ventas[producto["codigo"]] = [0, 0, 0, 0, 0]
    return ventas


def catalogo_inicial():
    productos = []
    for producto in CATALOGO_INICIAL:
        productos.append({
            "codigo": producto["codigo"],
            "nombre": producto["nombre"],
            "precio": producto["precio"],
        })
    return productos


def cargar_datos():
    productos = []
    try:
        archivo = open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split("|")
            productos.append({
                "codigo": int(partes[0]),
                "nombre": partes[1],
                "precio": int(partes[2]),
            })
        archivo.close()
    except FileNotFoundError:
        print("Primer dia de uso: se carga el catalogo inicial.")
        productos = catalogo_inicial()
    ventas = crear_ventas_vacias(productos)
    try:
        archivo = open(ARCHIVO_VENTAS, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split("|")
            codigo = int(partes[0])
            if buscar_producto(productos, codigo) is not None:
                cantidades = []
                for valor in partes[1:]:
                    cantidades.append(int(valor))
                ventas[codigo] = cantidades
        archivo.close()
    except FileNotFoundError:
        print("No habia ventas guardadas.")
    return productos, ventas


def guardar_datos(productos, ventas):
    archivo = open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8")
    for producto in productos:
        linea = str(producto["codigo"]) + "|" + producto["nombre"] + "|" + str(producto["precio"])
        archivo.write(linea + "\n")
    archivo.close()
    archivo = open(ARCHIVO_VENTAS, "w", encoding="utf-8")
    for producto in productos:
        codigo = producto["codigo"]
        cantidades = ventas[codigo]
        linea = str(codigo)
        for cantidad in cantidades:
            linea = linea + "|" + str(cantidad)
        archivo.write(linea + "\n")
    archivo.close()


def agregar_producto(productos, ventas):
    codigo = leer_entero("Codigo del producto: ")
    if buscar_producto(productos, codigo) is not None:
        print("Ese codigo ya existe. No se cargo.")
        return
    nombre = input("Nombre: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacio.")
        nombre = input("Nombre: ").strip()
    precio = leer_entero("Precio: ")
    while precio <= 0:
        print("El precio tiene que ser mayor a 0.")
        precio = leer_entero("Precio: ")
    productos.append({"codigo": codigo, "nombre": nombre, "precio": precio})
    ventas[codigo] = [0, 0, 0, 0, 0]
    guardar_datos(productos, ventas)
    print("Producto agregado.")


def registrar_venta(productos, ventas):
    dia = leer_entero("Dia (1 = lunes ... 5 = viernes): ")
    while dia < 1 or dia > 5:
        print("El dia tiene que estar entre 1 y 5.")
        dia = leer_entero("Dia (1 = lunes ... 5 = viernes): ")
    codigo = leer_entero("Codigo del producto: ")
    producto = buscar_producto(productos, codigo)
    if producto is None:
        print("Ese codigo no esta en el catalogo.")
        return
    cantidad = leer_entero("Cantidad: ")
    while cantidad <= 0:
        print("La cantidad tiene que ser mayor a 0.")
        cantidad = leer_entero("Cantidad: ")
    indice = dia - 1
    ventas[codigo][indice] = ventas[codigo][indice] + cantidad
    guardar_datos(productos, ventas)
    print("Venta registrada:", cantidad, producto["nombre"], "el", DIAS[indice])


def mostrar_informes(productos, ventas):
    print("")
    print("Unidades vendidas de cada producto")
    for producto in productos:
        unidades = unidades_producto(ventas, producto["codigo"])
        print("-", producto["nombre"] + ":", unidades)
    print("")
    print("Recaudacion de cada dia")
    for dia in range(1, 6):
        print("-", DIAS[dia - 1] + ":", recaudacion_dia(productos, ventas, dia))
    print("")
    mas_vendidos = productos_mas_vendidos(productos, ventas)
    if len(mas_vendidos) == 0:
        print("No hay producto mas vendido porque no hubo ventas.")
    elif len(mas_vendidos) == 1:
        producto = mas_vendidos[0]
        print("Producto mas vendido:", producto["nombre"], "-", unidades_producto(ventas, producto["codigo"]), "unidades")
    else:
        print("Empate en el producto mas vendido:")
        for producto in mas_vendidos:
            print("-", producto["nombre"], "-", unidades_producto(ventas, producto["codigo"]), "unidades")
    mejores_dias = dias_mayor_recaudacion(productos, ventas)
    if len(mejores_dias) == 0:
        print("No hay dia de mayor recaudacion porque no hubo ventas.")
    elif len(mejores_dias) == 1:
        dia = mejores_dias[0]
        print("Dia de mayor recaudacion:", DIAS[dia - 1], "-", recaudacion_dia(productos, ventas, dia))
    else:
        print("Empate en el dia de mayor recaudacion:")
        for dia in mejores_dias:
            print("-", DIAS[dia - 1], "-", recaudacion_dia(productos, ventas, dia))
    print("")
    print("Productos que no se vendieron")
    sin_ventas = productos_sin_ventas(productos, ventas)
    if len(sin_ventas) == 0:
        print("- todos los productos tuvieron alguna venta")
    else:
        for producto in sin_ventas:
            print("-", producto["nombre"])
    print("")
    print("Recaudacion total de la semana:", recaudacion_total(productos, ventas))
    print("")


def main():
    print("Buffet de la Facultad")
    productos, ventas = cargar_datos()
    guardar_datos(productos, ventas)
    while True:
        print("1. Registrar una venta")
        print("2. Ver informes de la semana")
        print("3. Agregar un producto")
        print("4. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            registrar_venta(productos, ventas)
        elif opcion == "2":
            mostrar_informes(productos, ventas)
        elif opcion == "3":
            agregar_producto(productos, ventas)
        elif opcion == "4":
            guardar_datos(productos, ventas)
            print("Datos guardados. Hasta manana.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
