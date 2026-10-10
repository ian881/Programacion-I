// Borrador. Primera version, incompleta.
// Tiene el menu y el registro de una venta.
Algoritmo borradorBuffet
	Dimension ventas[6, 5]
	Definir opcion, dia, fila, cantidad Como Entero
	opcion <- 0
	Mientras opcion <> 4 Hacer
		Escribir "1 Registrar venta"
		Escribir "2 Ver informes"
		Escribir "3 Agregar producto"
		Escribir "4 Salir"
		Leer opcion
		Si opcion = 1 Entonces
			Escribir "Numero de producto"
			Leer fila
			Escribir "Dia del 1 al 5"
			Leer dia
			Escribir "Cantidad"
			Leer cantidad
			ventas[fila, dia] <- ventas[fila, dia] + cantidad
			Escribir "Venta anotada"
		FinSi
	FinMientras
FinAlgoritmo
