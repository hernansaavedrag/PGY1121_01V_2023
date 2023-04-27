Proceso ejerSi2
	
	definir num1,num2 como entero;
	
	Escribir "Ingrese número 1: ";
	leer num1;
	escribir "Ingrese número 2: ";
	leer num2;
	
	si num1 > num2 Entonces
		Escribir "El número 1 es mayor que el número 2";
	SiNo
		si num2 > num1 Entonces
			Escribir "El número 2 es mayor que el número 1";
		SiNo
			Escribir "los números son iguales.";
		FinSi
	FinSi
	
FinProceso
