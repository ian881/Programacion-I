El buffet de la Facultad

Programación I
Actividad de Evaluación N.º 2

Nombre y apellido: Herrera
DNI: 45098991
Fecha: 10 de octubre de 2026

1. Problema y estructura de datos

Marta anota, de lunes a viernes, lo que se vende en el buffet de la Facultad. Entran dos grupos de datos. El catálogo trae el código, el nombre y el precio de cada producto. Cada venta trae el día, el código del producto y la cantidad. El programa acumula esas cantidades y al final de la semana muestra las unidades vendidas de cada producto, la recaudación de cada día, el producto más vendido, el día de mayor recaudación, los productos que no se vendieron y la recaudación total.

Elegí dos estructuras, porque los datos no cambian de la misma forma.

El catálogo es una lista de registros. Cada registro guarda juntos el código, el nombre y el precio. Así el precio del café no se puede mezclar con el nombre de otro producto. La otra opción era usar tres listas paralelas, una de códigos, una de nombres y una de precios. La descarté porque si se corre un índice, los datos de un producto quedan cruzados con los de otro.

Las ventas son una matriz. Cada fila es un producto y cada columna es un día, de lunes a viernes. El total de un producto es la suma de su fila. La recaudación de un día se obtiene recorriendo esa columna y multiplicando cada cantidad por el precio. La otra opción era guardar una lista de ventas sueltas, por ejemplo “el martes, 25 cafés”. La descarté porque para sacar el total de un producto o de un día hay que recorrer toda la lista.

Esas dos estructuras se guardan en archivos de texto: productos.txt y ventas.txt. Si quedaran solo en memoria, al cerrar el programa se perdería la semana. Con los archivos, Marta puede cerrar a la tarde y al otro día seguir con lo ya cargado. Alcanza con leerlos de principio a fin, porque son pocos productos y cinco días.

2. Diseño

El pseudocódigo está en buffet.psc. La lógica tiene tres momentos.

Al abrir, el programa se fija si ya existen los archivos. Si no existen, es el primer día: carga el catálogo inicial de seis productos y deja la matriz de ventas en cero. Si existen, recupera el catálogo y las cantidades de la semana.

Después entra a un menú que se repite mientras Marta no elija salir. Se usa un mientras, porque no se sabe cuántas operaciones va a hacer. Las opciones son registrar una venta, ver los informes, agregar un producto y salir.

Cuando registra una venta, pide el día y el código. Recorre el catálogo hasta encontrar ese código. Si no está, avisa y no carga nada. Si está, pide la cantidad y la suma en la fila de ese producto y la columna de ese día. Si el mismo producto se anota otra vez el mismo día, no se borra lo anterior: se suma.

Al salir, escribe los dos archivos. Por eso, la próxima vez que se abre, la semana sigue.

3. Codificación

El programa está en buffet.py. El menú es un while, porque la cantidad de vueltas no se conoce de antemano. Para recorrer los productos y los días se usa for, porque ahí la cantidad sí se conoce. En buscar_producto el for corta con break cuando encuentra el código, así no sigue hasta el final si ya lo halló.

Las funciones devuelven un valor. buscar_producto devuelve el registro o nada. unidades_producto devuelve la suma de la fila. recaudacion_dia devuelve la plata de un día. recaudacion_total devuelve la plata de la semana. productos_mas_vendidos, dias_mayor_recaudacion y productos_sin_ventas devuelven las listas que usa el informe. Si dos productos empatan, se muestran los dos. Lo mismo si empatan dos días.

Los procedimientos no devuelven nada. registrar_venta pide el día, el código y la cantidad, y suma. mostrar_informes imprime los cinco informes. agregar_producto suma un producto nuevo y no deja repetir el código. guardar_datos escribe los dos archivos.

No hay listas globales. El catálogo y las ventas se crean en el programa principal y se pasan por parámetro. Los nombres de los archivos y el catálogo inicial están al principio porque no cambian durante la ejecución.

Con los datos del cuaderno, la cuenta hecha a mano da: café 138, medialuna 203, sándwich 54, agua 115, empanada 78 y chipá 0. La recaudación es lunes 129000, martes 107700, miércoles 129900, jueves 161100 y viernes 127200. El más vendido es la medialuna, con 203 unidades. El día de mayor recaudación es el jueves, con 161100. El chipá no se vende. El total de la semana es 654900.

El programa guarda después de cada venta y también al salir. Así no se pierde el día si se cierra mal. El archivo es chico, entonces escribirlo seguido no es un problema.

4. Pruebas

Las cuatro pruebas se ejecutaron en la Terminal con python3 buffet.py. Antes de las pruebas de primer día se borraron productos.txt y ventas.txt.

Prueba 1. Archivo inexistente.
Entrada: abrir el programa sin los archivos.
Esperado: aviso de primer día y carga del catálogo inicial.
Obtenido: “Primer dia de uso: se carga el catalogo inicial” y “No habia ventas guardadas”.
Coincide: sí.
[Pegar acá la captura del menú recién abierto.]

Prueba 2. Vacío.
Entrada: opción 2, ver informes, sin ninguna venta cargada.
Esperado: todas las unidades en 0, recaudación 0, sin producto más vendido y los seis productos sin ventas.
Obtenido: el total de la semana fue 0 y el programa informó que no hay producto más vendido ni día de mayor recaudación.
Coincide: sí.
[Pegar acá la captura de los informes en cero.]

Prueba 3. Dato duplicado.
Entrada: el lunes, 30 cafés con leche (código 101) y después otros 5 cafés el mismo lunes.
Esperado: no es un error. Las dos ventas se suman y quedan 35 cafés. El lunes recauda 35 x 1500 = 52500.
Obtenido: “Cafe con leche: 35”, “lunes: 52500” y recaudación total 52500.
Coincide: sí.
[Pegar acá la captura del café en 35.]

Prueba 4. Dato que puede romper el programa.
Entrada: en el día se escribe “lunes” en vez de un número, y después el código 999, que no existe.
Esperado: el programa no se cierra. Vuelve a pedir el día y avisa que el código no está.
Obtenido: “Ingrese un numero entero” y “Ese codigo no esta en el catalogo”.
Coincide: sí.
[Pegar acá la captura del texto “lunes” y del código 999.]

5. Reflexión

Descarté la lista de ventas sueltas porque obliga a recorrer todo cada vez que Marta pide el total de un producto o de un día. También descarté las tres listas paralelas para el catálogo, porque un índice corrido mezcla el nombre de un producto con el precio de otro.

La matriz por código hace fáciles esas dos cuentas, y dos ventas del mismo producto el mismo día se suman solas. El límite aparece si el buffet abre los sábados: la lista deja de tener cinco posiciones y hay que modificar la carga, los archivos y los informes. Si agregan un producto a mitad de semana, el programa ya lo permite: se suma un registro nuevo y una fila de ceros, sin perder las ventas anteriores.
