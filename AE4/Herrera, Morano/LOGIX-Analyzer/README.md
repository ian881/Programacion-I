# LOGIX-Analyzer

Prototipo del TIFAS 2026 (AE4 intercátedra: Ingeniería de Requerimientos I, Matemática Discreta y Programación I).
Implementa los requerimientos funcionales RF1 a RF8 de la consigna, en Python estructurado y sin bibliotecas externas.

## Cómo se ejecuta

Desde esta carpeta (la que contiene `main.py`):

```
python main.py      # menú del programa
python pruebas.py   # 28 casos de prueba (Tablas 2, 5 y 6 y casos límite)
```

Al pedir un archivo, Enter usa los datos del caso LOGIX.

## Archivos

| Archivo | Contenido |
|---|---|
| `main.py` | Menú: pide los datos, llama a las funciones de `calculos.py` y muestra los resultados |
| `calculos.py` | Funciones de cálculo de RF1 a RF8 (no piden ni muestran datos) |
| `pruebas.py` | Casos de prueba con los resultados de la resolución manual |
| `datos/` | Tablas del caso: grafo G (Tabla 2), grafo G′, subgrafo del Anexo, red (Tabla 5), red con drones y sistema (Tabla 6) |
| `datos/casos_limite/` | Datos que el programa debe rechazar o informar de forma especial |

## Menú

| Opción | Requerimiento | Qué muestra |
|---|---|---|
| 1 | RF1 | Carga hasta 15 módulos y su matriz de adyacencia desde un archivo |
| 2 | RF2 | Grado de salida y de entrada de cada módulo |
| 3 | RF3 y RF4 | Matriz A*, los módulos afectados al modificar un módulo (columna) y los módulos en ciclos (diagonal) |
| 4 | RF5 | Determinante, si el sistema es compatible determinado y la solución (hasta 5 × 5) |
| 5 | RF6 | Punto de equilibrio entre dos alternativas (costo fijo y costo anual de cada una) |
| 6 | RF7 | Todos los caminos simples entre dos nodos, de menor a mayor tiempo; el primero es el mínimo |
| 7 | RF8 | Orden de migración (o el aviso de que el grafo tiene ciclos) |

Datos para la opción 5: A = `0;110`, B = `273;45`, C = `420;40` (costo fijo; costo anual, en miles de u.m.).
Por ejemplo, A frente a B se ingresa `0;110;273;45` y da 4,2 años y 462.
