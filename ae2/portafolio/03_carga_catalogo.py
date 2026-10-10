
catalogo = []


def buscar_codigo(productos, codigo):
    encontrado = None
    for producto in productos:
        if producto["codigo"] == codigo:
            encontrado = producto
            break
    return encontrado


def cargar_inicial(productos):
    iniciales = [
        {"codigo": 101, "nombre": "Cafe con leche", "precio": 1500},
        {"codigo": 102, "nombre": "Medialuna", "precio": 700},
        {"codigo": 103, "nombre": "Sandwich de miga", "precio": 1800},
        {"codigo": 104, "nombre": "Agua mineral 500 ml", "precio": 1000},
        {"codigo": 105, "nombre": "Empanada", "precio": 1200},
        {"codigo": 106, "nombre": "Chipa (100 g)", "precio": 1300},
    ]
    for producto in iniciales:
        if buscar_codigo(productos, producto["codigo"]) is None:
            productos.append(producto)
        else:
            print("El codigo", producto["codigo"], "ya existe. No se cargo.")


def agregar_producto(productos):
    codigo = int(input("Codigo: "))
    if buscar_codigo(productos, codigo) is not None:
        print("Ese codigo ya existe. No se cargo.")
        return
    nombre = input("Nombre: ")
    precio = int(input("Precio: "))
    productos.append({"codigo": codigo, "nombre": nombre, "precio": precio})
    print("Producto cargado.")


cargar_inicial(catalogo)
print("Catalogo cargado:")
for producto in catalogo:
    print(producto["codigo"], producto["nombre"], producto["precio"])
