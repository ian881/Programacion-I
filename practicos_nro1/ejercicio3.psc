//Ejercicio 3 - Ahorros de Mateo
//Mateo quiere comprar unos auriculares que cuestan 4500 pesos. Durante 5 semanas, su mama
//le dio una mesada de 700 pesos. Ademas, por cortar el pasto de su abuela dos veces recibio
//600 pesos en total. Por otro lado, su hermana gano 1200 pesos por ayudar en la verduleria
//y 350 pesos por pasear al perro. Se pide calcular cuanto dinero tiene Mateo en total y
//determinar si con ese dinero le alcanza para comprar los auriculares o si todavia le falta,
//mostrando el resultado en pantalla.
Algoritmo ejercicio3
	definir mesada, cortarPasto, totalMateo, auriculares Como Entero
	auriculares<-4500
	mesada<-700*5
	cortarPasto<-600
	totalMateo<-(mesada+cortarPasto)
	escribir"el total de dinero que tiene mateo es de ", totalMateo
	escribir"los auriculares cuestan ", auriculares
	si (totalMateo >= auriculares) Entonces
		escribir"le alcanza el dinero para comprar los auriculares"
	SiNo
		escribir"no le alcanza ya que le falta ", (auriculares-totalMateo)
	fin si
FinAlgoritmo
