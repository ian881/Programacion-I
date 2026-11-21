"""LOGIX-Analyzer (TIFAS 2026 - AE4). Menú: pide los datos, llama a calculos.py y muestra los resultados."""
import calculos


def pedir_ruta(defecto):
    """Pide el archivo de datos; con Enter usa el archivo del caso LOGIX."""
    ruta = input("Archivo [Enter = " + defecto + "]: ").strip()
    if ruta == "":
        ruta = defecto
    return ruta


def pedir_posicion(nombres, mensaje):
    """Pide un nombre y devuelve su posición con la búsqueda lineal; si no existe, informa el error."""
    posicion = calculos.buscar(nombres, input(mensaje).strip().upper())
    if posicion == -1:
        raise ValueError("ese nombre no está en los datos cargados")
    return posicion


def main():
    """Menú principal: se repite hasta elegir 0. Empieza con el grafo G de la Tabla 2 ya cargado."""
    nombres, a = calculos.cargar_grafo("datos/logix_dependencias.csv")
    opcion = ""
    while opcion != "0":
        print("\nLOGIX-Analyzer | 1 Cargar módulos [RF1] | 2 Grados [RF2] | 3 Alcanzabilidad [RF3-RF4]\n"
              "4 Sistema [RF5] | 5 Equilibrio [RF6] | 6 Camino mínimo [RF7] | 7 Orden de migración [RF8] | 0 Salir")
        opcion = input("Opción: ").strip()
        try:
            if opcion == "1":
                nombres, a = calculos.cargar_grafo(pedir_ruta("datos/logix_dependencias.csv"))
                print("Se cargaron", len(nombres), "módulos:", " ".join(nombres))
            elif opcion == "2":
                salida, entrada = calculos.grados(a)
                for i in range(len(a)):
                    print(" ", nombres[i], "\tsalida:", salida[i], "\tentrada:", entrada[i])
            elif opcion == "3":
                estrella = calculos.alcanzabilidad(a)
                j = pedir_posicion(nombres, "Módulo que se modifica: ")
                afectados, en_ciclo = [], []
                for i in range(len(a)):
                    print(" ", nombres[i], estrella[i])            # fila i de A*
                    if estrella[i][j] == 1:
                        afectados.append(nombres[i])               # columna j: dependen de j (directa o indirectamente)
                    if estrella[i][i] == 1:
                        en_ciclo.append(nombres[i])                # diagonal: i vuelve a sí mismo
                print("Afectados por", nombres[j] + ":", " ".join(afectados), "\nEn ciclos:", " ".join(en_ciclo))
            elif opcion == "4":
                ab = calculos.cargar_sistema(pedir_ruta("datos/sistema_pilotos.csv"))
                det, solucion, tipo = calculos.gauss_jordan(ab)
                print("Determinante:", det, "- el sistema", tipo, "- solución:", solucion)
            elif opcion == "5":
                d = input("Costo fijo y costo anual de la alternativa 1 y de la 2, separados por ';': ").split(";")
                n, costo = calculos.equilibrio(float(d[0]), float(d[1]), float(d[2]), float(d[3]))
                print("Equilibrio a los", round(n, 2), "años, con un costo acumulado de", round(costo, 2))
            elif opcion == "6":
                nodos, w = calculos.cargar_red(pedir_ruta("datos/red_terrestre.csv"))
                origen = pedir_posicion(nodos, "Origen: ")
                caminos = []
                calculos.explorar(w, nodos, origen, pedir_posicion(nodos, "Destino: "), [nodos[origen]], 0, caminos)
                print(len(caminos), "caminos, de menor a mayor tiempo (el primero es el camino mínimo):")
                for par in caminos:
                    print(" ", par[0], "min\t" + "-".join(par[1]))
            elif opcion == "7":
                print("Orden de migración:", " → ".join(calculos.orden_migracion(a, nombres)))
        except (ValueError, OSError) as error:
            print("Atención:", error)
        except IndexError:
            print("Atención: faltan datos en lo que se ingresó o en el archivo")


main()
