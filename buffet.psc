// AE2 - El buffet de la Facultad
// Como se cargan, se procesan y se recuperan los datos.
// Cada producto es un registro: codigo, nombre y precio.
// Las ventas son una matriz: fila del producto, columna del dia.
Algoritmo buffet
	Definir producto Como Registro
		codigo Como Entero
		nombre Como Caracter
		precio Como Entero
	FinRegistro
	Dimension productos[6]
	Dimension ventas[6, 5]
	Definir opcion, i, j, dia, codigoBuscado, cantidad, pos Como Entero
	Definir hayArchivo Como Logico
	
	// Recuperar al abrir el programa
	// Falso = primer dia, todavia no existen los archivos
	// Verdadero = se leen productos.txt y ventas.txt
	hayArchivo <- Falso
	Si hayArchivo = Verdadero Entonces
		Escribir "Se recuperan el catalogo y las ventas de la semana"
	SiNo
		productos[1].codigo <- 101
		productos[1].nombre <- "Cafe con leche"
		productos[1].precio <- 1500
		productos[2].codigo <- 102
		productos[2].nombre <- "Medialuna"
		productos[2].precio <- 700
		productos[3].codigo <- 103
		productos[3].nombre <- "Sandwich de miga"
		productos[3].precio <- 1800
		productos[4].codigo <- 104
		productos[4].nombre <- "Agua mineral"
		productos[4].precio <- 1000
		productos[5].codigo <- 105
		productos[5].nombre <- "Empanada"
		productos[5].precio <- 1200
		productos[6].codigo <- 106
		productos[6].nombre <- "Chipa"
		productos[6].precio <- 1300
		Para i <- 1 Hasta 6 Con Paso 1 Hacer
			Para j <- 1 Hasta 5 Con Paso 1 Hacer
				ventas[i, j] <- 0
			FinPara
		FinPara
		Escribir "Primer dia: catalogo inicial y ventas en cero"
	FinSi
	
	opcion <- 0
	Mientras opcion <> 4 Hacer
		Escribir "1 Registrar venta  2 Informes  3 Agregar producto  4 Salir"
		Leer opcion
		Si opcion = 1 Entonces
			Escribir "Dia del 1 al 5"
			Leer dia
			Escribir "Codigo"
			Leer codigoBuscado
			pos <- 0
			Para i <- 1 Hasta 6 Con Paso 1 Hacer
				Si productos[i].codigo = codigoBuscado Entonces
					pos <- i
				FinSi
			FinPara
			Si pos = 0 Entonces
				Escribir "Codigo inexistente"
			SiNo
				Escribir "Cantidad"
				Leer cantidad
				ventas[pos, dia] <- ventas[pos, dia] + cantidad
				Escribir "Venta sumada"
			FinSi
		FinSi
		Si opcion = 4 Entonces
			Escribir "Se guardan productos.txt y ventas.txt"
		FinSi
	FinMientras
FinAlgoritmo
