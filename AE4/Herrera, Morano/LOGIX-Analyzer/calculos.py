"""LOGIX-Analyzer: funciones de cálculo de los requerimientos RF1 a RF8 (no piden ni muestran datos)."""
INF = float("inf")   # "no hay arista" en la matriz de pesos W
EPS = 1e-9           # tolerancia para comparar números reales con cero


def leer_csv(ruta):
    """Devuelve las filas de un archivo separado por ';', salteando líneas vacías y comentarios (#)."""
    filas = []
    archivo = open(ruta, encoding="utf-8")
    for linea in archivo:
        if linea.strip() != "" and not linea.startswith("#"):
            filas.append(linea.strip().split(";"))
    archivo.close()
    return filas


def buscar(lista, valor):
    """Búsqueda lineal: posición de 'valor' en la lista, o -1 si no está."""
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


def cargar_grafo(ruta):
    """RF1: nombres de los módulos (hasta 15) y matriz de adyacencia A: a[i][j] = 1 si i depende de j."""
    filas = leer_csv(ruta)
    if len(filas) < 2 or len(filas) > 16 or len(filas[0]) != len(filas):
        raise ValueError("se necesita una matriz cuadrada de 1 a 15 módulos, con sus nombres")
    nombres, a = filas[0][1:], []
    for fila in filas[1:]:
        if len(fila) != len(filas) or fila[0] != nombres[len(a)]:
            raise ValueError("cada fila debe empezar con su módulo y tener un valor por módulo")
        a.append([])
        for valor in fila[1:]:
            if valor != "0" and valor != "1":
                raise ValueError("los valores de la matriz deben ser 0 o 1")
            a[-1].append(int(valor))
    return nombres, a


def grados(a):
    """RF2: grado de salida (suma de la fila) y grado de entrada (suma de la columna) de cada módulo."""
    salida, entrada = [0] * len(a), [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            salida[i] = salida[i] + a[i][j]
            entrada[j] = entrada[j] + a[i][j]
    return salida, entrada


def producto_booleano(x, y):
    """(X ⊙ Y)[i][j] = 1 si existe algún k con X[i][k] = 1 y Y[k][j] = 1."""
    n = len(x)
    r = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if x[i][k] == 1 and y[k][j] == 1:
                    r[i][j] = 1
    return r


def alcanzabilidad(a):
    """RF3 y RF4: A* = A ∨ A² ∨ ... ∨ Aⁿ, sin la identidad. Columna j: afectados por j; diagonal: ciclos."""
    n = len(a)
    potencia = a
    acumulada = [[0] * n for _ in range(n)]
    for paso in range(n):
        for i in range(n):
            for j in range(n):
                acumulada[i][j] = max(acumulada[i][j], potencia[i][j])   # acumulada ∨ potencia
        potencia = producto_booleano(potencia, a)                          # Aᵏ⁺¹ = Aᵏ ⊙ A
    return acumulada


def orden_migracion(a, nombres):
    """RF8: orden topológico con una COLA. Si quedan módulos sin ubicar, el grafo tiene ciclos."""
    pendientes = grados(a)[0]             # dependencias de cada módulo que todavía no se migraron
    cola, orden = [], []
    for i in range(len(a)):
        if pendientes[i] == 0:
            cola.append(i)                # encolar los que no dependen de nadie
    while len(cola) > 0:
        j = cola.pop(0)                   # desencolar: sale el primero que entró
        orden.append(nombres[j])
        for i in range(len(a)):           # columna j: los módulos que dependen de j
            if a[i][j] == 1:
                pendientes[i] = pendientes[i] - 1
                if pendientes[i] == 0:
                    cola.append(i)
    if len(orden) < len(a):
        raise ValueError("el grafo tiene dependencias circulares: no existe un orden de migración")
    return orden


def cargar_sistema(ruta):
    """RF5: matriz ampliada [M | B]; cada fila tiene los coeficientes y el término independiente."""
    ab = leer_csv(ruta)
    if len(ab) < 1 or len(ab) > 5:
        raise ValueError("el sistema debe tener de 1 a 5 ecuaciones")
    for fila in ab:
        if len(fila) != len(ab) + 1:
            raise ValueError("cada ecuación necesita un coeficiente por incógnita y el término independiente")
        for k in range(len(fila)):
            fila[k] = float(fila[k])
    return ab


def gauss_jordan(ab):
    """RF5: método del pivote. Devuelve determinante, solución y si el sistema es compatible determinado."""
    n = len(ab)
    det = 1.0
    for col in range(n):
        p = col
        while p < n and abs(ab[p][col]) < EPS:                # busca una fila con pivote no nulo
            p = p + 1
        if p == n:
            return 0.0, [], "NO es compatible determinado (det = 0)"
        if p != col:
            for k in range(n + 1):
                ab[col][k] = ab[col][k] + ab[p][k]            # F_col ← F_col + F_p (no cambia el det)
        pivote = ab[col][col]
        det = det * pivote                                     # det(M) = producto de los pivotes
        for k in range(n + 1):
            ab[col][k] = ab[col][k] / pivote                   # el pivote queda en 1
        for r in range(n):
            if r != col:
                factor = ab[r][col]
                for k in range(n + 1):
                    ab[r][k] = ab[r][k] - factor * ab[col][k]  # ceros arriba y abajo del pivote
    solucion = []
    for r in range(n):
        solucion.append(round(ab[r][n], 6))
    return round(det, 6), solucion, "es compatible determinado"


def equilibrio(fijo1, anual1, fijo2, anual2):
    """RF6: corte de C = fijo1 + anual1·n con C = fijo2 + anual2·n, por Cramer. Devuelve n y C."""
    det = anual2 - anual1
    if abs(det) < EPS:
        raise ValueError("los costos anuales son iguales: rectas paralelas, no hay punto de equilibrio")
    return (fijo1 - fijo2) / det, (anual2 * fijo1 - anual1 * fijo2) / det


def cargar_red(ruta):
    """RF7: lee las aristas 'origen;destino;minutos' y arma la matriz de pesos W (grafo no dirigido)."""
    aristas = leer_csv(ruta)[1:]
    nodos = []
    for f in aristas:
        for nodo in f[:2]:
            if buscar(nodos, nodo) == -1:
                nodos.append(nodo)
    w = [[INF] * len(nodos) for _ in range(len(nodos))]
    for f in aristas:
        if float(f[2]) < 0:
            raise ValueError("un tiempo de recorrido no puede ser negativo")
        w[buscar(nodos, f[0])][buscar(nodos, f[1])] = float(f[2])
        w[buscar(nodos, f[1])][buscar(nodos, f[0])] = float(f[2])
    return nodos, w


def explorar(w, nodos, actual, destino, camino, costo, caminos):
    """RF7, RECURSIVO: recorre todos los caminos simples hasta 'destino' y guarda cada uno con su
    costo en 'caminos', insertándolo en su lugar (inserción) para que queden de menor a mayor."""
    if actual == destino:                                  # caso base: se llegó al destino
        j = len(caminos)
        while j > 0 and caminos[j - 1][0] > costo:        # retrocede mientras el anterior sea más caro
            j = j - 1
        caminos.insert(j, [costo, camino[:]])              # inserción ordenada: queda de menor a mayor
        return
    for v in range(len(w)):
        if w[actual][v] != INF and buscar(camino, nodos[v]) == -1:
            camino.append(nodos[v])                        # apilar
            explorar(w, nodos, v, destino, camino, costo + w[actual][v], caminos)
            camino.pop()                                   # desapilar y probar el vecino siguiente
