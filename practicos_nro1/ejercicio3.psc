//Ejercicio 3 - Ahorros de Mateo

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
