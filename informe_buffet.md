# El buffet de la Facultad

Programación I · Práctica de estructuras de datos

Nombre y apellido: Herrera  
DNI: 45098991  
Fecha: 9 de octubre de 2026

## 1. Problema y elección de estructuras

### 1.1 El problema

Marta anota, de lunes a viernes, qué se vendió en el buffet. Entran dos grupos de datos: el catálogo (código, nombre y precio) y cada venta (día, código y cantidad). El programa acumula esas cantidades y al final de la semana informa unidades por producto, recaudación por día, el producto más vendido, el día de mayor recaudación, los productos sin ventas y el total de la semana.

### 1.2 Qué hay que guardar

Casi no cambian: código, nombre y precio de cada producto. Cambian todos los días: la cantidad vendida de cada producto en cada día. Por eso el catálogo y las ventas no van en la misma estructura. El catálogo se carga una vez y las ventas se actualizan en cada registro.

### 1.3 Dos formas de guardar las ventas

Opción A, una matriz de cantidades. Cada fila es un producto y cada columna es un día. El martes del cuaderno quedaría así:

| Código | Lun | Mar | Mié | Jue | Vie |
|---|---|---|---|---|---|
| 101 | 0 | 25 | 0 | 0 | 0 |
| 102 | 0 | 38 | 0 | 0 | 0 |
| 103 | 0 | 12 | 0 | 0 | 0 |
| 104 | 0 | 22 | 0 | 0 | 0 |
| 105 | 0 | 0 | 0 | 0 | 0 |
| 106 | 0 | 0 | 0 | 0 | 0 |

Opción B, una lista de ventas sueltas. El martes serían cuatro registros: (2, 101, 25), (2, 102, 38), (2, 103, 12) y (2, 104, 22).

Elegí la opción A. El total de un producto es la suma de su fila y el total de un día es la suma de su columna. En la opción B hay que recorrer toda la lista para cualquiera de los dos totales.

En el programa la matriz está guardada como un diccionario: la clave es el código y el valor es una lista de 5 cantidades. El acceso es directo por código y no se mezclan las filas si se agrega un producto.

### 1.4 Qué pasa si solo está en memoria

Si Marta cierra el programa, la memoria se borra y al otro día la semana empieza vacía. Eso se resuelve con archivos de texto. Se guarda el catálogo completo y, para cada código, las 5 cantidades de la semana.

### 1.5 Cómo guardar código, nombre y precio

Opción 1: tres listas paralelas (códigos, nombres y precios). Hay que cuidar que el índice 0 de las tres sea el mismo producto. Opción 2: una lista de registros, y cada registro tiene los tres datos juntos.

Elegí la opción 2. Un producto es un diccionario `{"codigo", "nombre", "precio"}`. No se puede desordenar el nombre de un producto respecto de su precio.

### 1.6 Archivos

Hacen falta dos:

- `productos.txt`: archivo maestro del catálogo. Función: conservar código, nombre y precio.
- `ventas.txt`: archivo de movimientos acumulados. Función: conservar las cantidades de la semana.

Los dos se leen de principio a fin, así que alcanza con organización secuencial. No hace falta ir directo a un byte del archivo: son 6 productos y 5 días.

## 2. Diseño

### 2.1 Menú

Marta elige con un menú: registrar una venta, ver informes, agregar un producto o salir. El menú está dentro de un `mientras`, porque no se sabe cuántas operaciones va a hacer. Un `para` no sirve: exigiría conocer la cantidad de vueltas antes de empezar.

### 2.2 Carga al arrancar

Al abrir, el programa intenta leer los dos archivos. Si no existen, es el primer día: carga el catálogo inicial de 6 productos y deja las ventas en cero. Si existen, recupera lo ya anotado y Marta sigue la semana.

### 2.3 Procesamiento

Si anota 3 empanadas el miércoles, se busca el código 105 y se suma 3 en la posición del miércoles. Si ese mismo día vuelve a anotar empanadas, se suman a las que ya estaban. No se pisan.

El total de un producto es la suma de sus 5 días. El total de un día es cantidad por precio de cada producto, sumados.

### 2.4 Recuperación

El jueves, al abrir, lee `productos.txt` y `ventas.txt` y vuelve a armar la lista de registros y la matriz. Lo del lunes, martes y miércoles sigue en esas filas.

## 3. Codificación

El programa está en `buffet.py`.

### 3.1 Ciclos

- `while` en el menú y al pedir un entero válido, porque la cantidad de intentos no se conoce.
- `for` para recorrer productos y días, porque la cantidad sí se conoce.
- En `buscar_producto` el `for` puede cortar antes del final con `break` cuando encuentra el código.

### 3.2 Subprogramas

Funciones, devuelven un valor:

| Función | Recibe | Para qué |
|---|---|---|
| `buscar_producto` | la lista y un código | devolver el registro o nada |
| `unidades_producto` | las ventas y un código | devolver la suma de la fila |
| `recaudacion_dia` | productos, ventas y el día | devolver la plata de ese día |
| `recaudacion_total` | productos y ventas | devolver la plata de la semana |
| `productos_mas_vendidos` | productos y ventas | devolver la lista de los que empatan en el máximo |
| `dias_mayor_recaudacion` | productos y ventas | devolver los días que empatan en recaudación |
| `productos_sin_ventas` | productos y ventas | devolver los que están en cero |

Procedimientos, no devuelven nada:

| Procedimiento | Recibe | Para qué |
|---|---|---|
| `registrar_venta` | productos y ventas | pedir día, código y cantidad, y sumar |
| `mostrar_informes` | productos y ventas | imprimir los 5 informes |
| `agregar_producto` | productos y ventas | sumar un producto nuevo sin código repetido |
| `guardar_datos` | productos y ventas | escribir los dos archivos |
| `cargar_datos` | nada, lee los archivos | armar de nuevo las dos estructuras |

`cargar_datos` devuelve las dos estructuras, así que funciona como función. Los otros cuatro de esa tabla son procedimientos.

### 3.3 Variables globales

No hay listas globales. Productos y ventas viven en `main` y se pasan por parámetro. Así una función no modifica otra cosa sin que se note. Los nombres de los archivos, los días y el catálogo inicial sí están arriba del programa, porque no cambian durante la ejecución. Pasarlos por parámetro en cada llamada alargaría el código sin ganar nada.

### 3.4 Informes calculados a mano con el cuaderno

Unidades: café 138, medialuna 203, sándwich 54, agua 115, empanada 78, chipá 0.

Recaudación: lunes 129000, martes 107700, miércoles 129900, jueves 161100, viernes 127200.

Más vendido: medialuna, 203 unidades. Día de mayor recaudación: jueves, 161100. Sin ventas: chipá. Total de la semana: 654900.

Si dos productos empatan en unidades, se muestran los dos. Lo mismo si dos días empatan en plata. No se elige uno solo.

### 3.5 Persistencia

Se guarda después de cada venta, después de agregar un producto y también al salir. Guardar en cada venta evita perder el día si se corta la luz antes de elegir salir. El riesgo es que un error a mitad de la escritura deje el archivo a medias. Guardar solo al salir es más simple, pero se pierde todo lo del día si el programa se cierra mal. Elegí guardar en cada cambio porque el archivo es chico.

## 4. Pruebas

Los resultados de abajo salieron de ejecutar `buffet.py`.

| N° | Entrada | Esperado | Obtenido | Coincide |
|---|---|---|---|---|
| 4.1 | Semana del cuaderno, cargada sobre las funciones del programa | Medialuna 203, jueves 161100, chipá sin ventas, total 654900 | Medialuna 203, jueves 161100, chipá sin ventas, total 654900 | Sí |
| 4.2 | Abrir y pedir informes sin ventas | Todo en 0, sin producto más vendido, los 6 sin ventas, total 0 | El mismo mensaje | Sí |
| 4.3 | Borrar los archivos y abrir | Aviso de primer día y catálogo inicial de 6 productos | Apareció "Primer dia de uso" y se crearon los archivos | Sí |
| 4.4 | El lunes, 30 cafés y después otros 5 cafés | No es un error: quedan 35 cafés el lunes | El archivo quedó `101\|35\|0\|0\|0\|0` | Sí |
| 4.5 | Poner "lunes" en lugar del número de día, y un código que no existe | No se cae el programa: vuelve a pedir el día y avisa código inexistente | Pidió otra vez el día y mostró "Ese codigo no esta en el catalogo" | Sí |

Otra prueba de cierre: se registraron 30 cafés y 40 medialunas, se salió, se volvió a abrir y los informes seguían en 30 y 40. El lunes daba 73000, que es 30 × 1500 + 40 × 700.

## 5. Reflexión

### 5.1 Qué descarté

Descarté la lista de ventas sueltas. Sirve para guardar el historial de cada anotación, pero para los informes de Marta obliga a recorrer todo cada vez. También descarté las tres listas paralelas para el catálogo, porque un índice corrido mezcla el precio de un producto con el nombre de otro.

### 5.2 Ventajas y límites

La matriz por código hace fáciles los totales por fila y por columna, y dos ventas del mismo producto el mismo día se suman solas. El límite aparece si el buffet abre los sábados: la lista deja de tener 5 posiciones y hay que tocar el alta, los archivos y los informes. Si agregan un producto a mitad de semana, el programa ya lo permite: se suma un registro y una fila de ceros, y no se pierden las ventas anteriores.

