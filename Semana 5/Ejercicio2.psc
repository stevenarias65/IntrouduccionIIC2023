Proceso sin_titulo
	//Un colegio desea saber qu� porcentaje de ni�os y qu� porcentaje de ni�as hay en el curso
	//actual. Dise�ar un algoritmo para este prop�sito. Recuerda que para calcular el porcentaje
//puedes hacer una regla de 3 simple. El programa debe solicitar al usuario que ingrese la
//cantidad total de ni�os, y la cantidad total de ni�as que hay en el curso.
	definir nenes, nenas, totalDeAlumnos Como Entero
	Definir  porcentajeNenas,porcentajeNenes Como Real
	
	Escribir "ingrese la cantidad total de ni�os: "
	leer nenes
	Escribir "ingrese la cantidad total de ni�as: "
	leer nenas
	totalDeAlumnos = (nenes+nenas)
	porcentajeNenas = ((nenas*100)/totalDeAlumnos)
	porcentajeNenes = ((nenes*100)/totalDeAlumnos)
	Escribir "el total de alumnos es de: " totalDeAlumnos " alumnos"
	Escribir "el porcentaje de ni�as es de: " porcentajeNenas "%"
	Escribir "el porcentaje de ni�os es de: " porcentajeNenes "%"	
	
FinProceso
