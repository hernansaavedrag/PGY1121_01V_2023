Proceso tablasMultiplicar
	
	Definir num,i,multi como entero;
	
	para num=1 hasta 10 con paso 1 hacer 
		Escribir "Tabla multiplicar del ",num;
		para i = 1 hasta 10 con paso 1 Hacer
			multi = num * i;
			Escribir num, " * ",i," = ",multi;
		FinPara
		Escribir "Presione Enter para continuar";
		Esperar Tecla;
		Limpiar Pantalla;
		
	FinPara
	
FinProceso
