Proceso tablaMultiplicar
	
	Definir num,i,multi como entero;
	
	Escribir "Ingrese número a multiplicar";
	leer num;
	
	si num > 0 Entonces
		Escribir "la tabla de multiplicar de: ",num;
		
		para i= 1 hasta 10 con paso 1 Hacer
			multi = num * i;
			Escribir num, " * ",i," = ",multi;
		FinPara
	SiNo
		Escribir "El numero debe ser mayor a cero";
	FinSi
	
	
	
FinProceso
