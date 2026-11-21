"""Casos de prueba de LOGIX-Analyzer: datos de las Tablas 2, 5 y 6 y casos límite. Se ejecuta con: python pruebas.py"""
import calculos

resultados = []   # una entrada True/False por prueba


def probar(codigo, descripcion, obtenido, esperado):
    """Compara el resultado del programa con el esperado (resolución manual) e informa la prueba."""
    resultados.append(obtenido == esperado)
    estado = "OK   "
    if obtenido != esperado:
        estado = "FALLA"
    print(estado, codigo, descripcion, "| esperado:", esperado, "| obtenido:", obtenido)


def rechaza(tipo, dato):
    """True si el programa rechaza el dato con ValueError (caso límite)."""
    try:
        if tipo == "grafo":
            calculos.cargar_grafo(dato)
        elif tipo == "sistema":
            calculos.cargar_sistema(dato)
        elif tipo == "red":
            calculos.cargar_red(dato)
        elif tipo == "orden":
            calculos.orden_migracion(dato[1], dato[0])
        else:
            calculos.equilibrio(dato[0], dato[1], dato[2], dato[3])
    except ValueError:
        return True
    return False


def unos(m, hasta):
    """Cantidad de unos de A* entre los primeros 'hasta' módulos (pares alcanzables)."""
    total = 0
    for i in range(hasta):
        for j in range(hasta):
            total = total + m[i][j]
    return total


def lista_de(nombres, m, columna):
    """Nombres de las filas que tienen un 1 en la columna indicada; con columna -1 lee la diagonal."""
    lista = []
    for i in range(len(m)):
        if (columna == -1 and m[i][i] == 1) or (columna != -1 and m[i][columna] == 1):
            lista.append(nombres[i])
    return lista


def caminos(ruta, origen, destino):
    """Caminos de origen a destino, de menor a mayor costo."""
    nodos, w = calculos.cargar_red(ruta)
    lista = []
    calculos.explorar(w, nodos, calculos.buscar(nodos, origen), calculos.buscar(nodos, destino), [origen], 0, lista)
    return lista


def main():
    """Ejecuta todas las pruebas y muestra el resumen."""
    limite = "datos/casos_limite/"
    nombres, a = calculos.cargar_grafo("datos/logix_dependencias.csv")
    salida, entrada = calculos.grados(a)
    estrella = calculos.alcanzabilidad(a)
    nombres2, a2 = calculos.cargar_grafo("datos/logix_reestructurado.csv")
    sub_nombres, sub = calculos.cargar_grafo("datos/anexo_subgrafo.csv")
    probar("P01", "RF1 Tabla 2: módulos y arcos", [len(nombres), sum(salida)], [9, 14])
    probar("P02", "RF1 16 módulos (máximo 15)", rechaza("grafo", limite + "grafo_16_modulos.csv"), True)
    probar("P03", "RF1 valor distinto de 0 y 1", rechaza("grafo", limite + "grafo_no_binario.csv"), True)
    probar("P04", "RF1 archivo vacío", rechaza("grafo", limite + "grafo_vacio.csv"), True)
    probar("P05", "RF2 grados de salida", salida, [3, 0, 1, 1, 2, 1, 1, 2, 3])
    probar("P06", "RF2 grados de entrada", entrada, [2, 1, 4, 1, 2, 1, 2, 1, 0])
    probar("P07", "RF3 pares de A* en G", unos(estrella, 9), 40)
    probar("P08", "RF3 afectados por INV (s4)", lista_de(nombres, estrella, 2),
           ["PED", "INV", "ROB", "ASG", "RUT", "SEG", "ENT", "REP"])
    probar("P09", "RF3 A* del subgrafo del Anexo", calculos.alcanzabilidad(sub),
           [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    probar("P10", "RF3 pares de A* en G′ (9 módulos originales)", unos(calculos.alcanzabilidad(a2), 9), 27)
    probar("P11", "RF4 módulos en ciclos en G", lista_de(nombres, estrella, -1), ["INV", "ROB", "ASG", "RUT", "SEG"])
    probar("P12", "RF4 G′ no tiene ciclos", lista_de(nombres2, calculos.alcanzabilidad(a2), -1), [])
    probar("P13", "RF5 Tabla 6", calculos.gauss_jordan(calculos.cargar_sistema("datos/sistema_pilotos.csv")),
           (11.0, [12.0, 20.0, 35.0], "es compatible determinado"))
    probar("P14", "RF5 primer pivote nulo", calculos.gauss_jordan(calculos.cargar_sistema(limite + "sistema_pivote_cero.csv"))[1],
           [1.0, 2.0, 3.0])
    probar("P15", "RF5 sistema incompatible", calculos.gauss_jordan(calculos.cargar_sistema(limite + "sistema_si.csv"))[0], 0.0)
    probar("P16", "RF5 sistema indeterminado", calculos.gauss_jordan(calculos.cargar_sistema(limite + "sistema_sci.csv"))[0], 0.0)
    probar("P17", "RF5 sistema 6 x 6 (máximo 5)", rechaza("sistema", limite + "sistema_6x6.csv"), True)
    probar("P18", "RF6 equilibrio A-B", calculos.equilibrio(0, 110, 273, 45), (4.2, 462.0))
    probar("P19", "RF6 equilibrio A-C", calculos.equilibrio(0, 110, 420, 40), (6.0, 660.0))
    probar("P20", "RF6 equilibrio B-C", calculos.equilibrio(273, 45, 420, 40), (29.4, 1596.0))
    probar("P21", "RF6 mismo costo anual (paralelas)", rechaza("equilibrio", [100, 50, 200, 50]), True)
    terrestre = caminos("datos/red_terrestre.csv", "D", "Z3")
    probar("P22", "RF7 red terrestre D-Z3", [len(terrestre), terrestre[0]], [13, [16.0, ["D", "H2", "Z2", "Z3"]]])
    probar("P23", "RF7 red con drones D-Z3", caminos("datos/red_con_drones.csv", "D", "Z3")[0], [14.0, ["D", "Z3"]])
    probar("P24", "RF7 red desconectada", caminos(limite + "red_desconectada.csv", "D", "Z3"), [])
    probar("P25", "RF7 tiempo negativo", rechaza("red", limite + "red_peso_negativo.csv"), True)
    probar("P26", "RF8 orden de migración de G′", calculos.orden_migracion(a2, nombres2),
           ["CLI", "BUS", "ROB", "SEG", "INV", "RUT", "ASG", "PED", "ENT", "REP"])
    probar("P27", "RF8 G con ciclos", rechaza("orden", [nombres, a]), True)
    probar("P28", "RF8 un único ciclo", rechaza("orden", calculos.cargar_grafo(limite + "grafo_ciclo_total.csv")), True)
    print("\nPruebas aprobadas:", resultados.count(True), "de", len(resultados))


main()
