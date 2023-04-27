Proceso ejerSi3
	
	definir num1,num2,num3, suma como entero;
	
	Escribir "Ingrese número 1:";
	leer num1;
	Escribir "Ingrese número 2:";
	leer num2;
	Escribir "Ingrese número 3:";
	leer num3;
	
	suma = num1+num2+num3;
	
	si suma > 10 Entonces
		Escribir "La suma es mayor a 10";
	SiNo
		si suma < 10 Entonces
			Escribir "La suma es menor que 10";
		SiNo
			Escribir "La suma es igual a 10";
		FinSi
	FinSi
	
	
FinProceso
