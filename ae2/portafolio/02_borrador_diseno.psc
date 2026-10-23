// Ian Herrera - DNI 45098991
// AE2 - Parte 2 de 4
// Borrador del buffet. Primera version, incompleta.
// Tiene el menu y el registro de una venta.
// Todavia no hice los informes ni los archivos.
Algoritmo borradorBuffet
	Dimension codigos[6]
	Dimension ventas[6, 5]
	Definir opcion, dia, codigo, cantidad, i, j, pos Como Entero
	
	codigos[1] <- 101
	codigos[2] <- 102
	codigos[3] <- 103
	codigos[4] <- 104
	codigos[5] <- 105
	codigos[6] <- 106
	
	Para i <- 1 Hasta 6 Con Paso 1 Hacer
		Para j <- 1 Hasta 5 Con Paso 1 Hacer
			ventas[i, j] <- 0
		FinPara
	FinPara
	
	opcion <- 0
	Mientras opcion <> 4 Hacer
		Escribir "1 Registrar venta"
		Escribir "2 Ver informes"
		Escribir "3 Agregar producto"
		Escribir "4 Salir"
		Leer opcion
		Si opcion = 1 Entonces
			Escribir "Codigo del producto"
			Leer codigo
			pos <- 0
			Para i <- 1 Hasta 6 Con Paso 1 Hacer
				Si codigos[i] = codigo Entonces
					pos <- i
				FinSi
			FinPara
			Si pos = 0 Entonces
				Escribir "Ese codigo no esta"
			SiNo
				Escribir "Dia (1 a 5)"
				Leer dia
				Escribir "Cantidad"
				Leer cantidad
				ventas[pos, dia] <- ventas[pos, dia] + cantidad
				Escribir "Venta anotada"
			FinSi
		FinSi
	FinMientras
FinAlgoritmo
