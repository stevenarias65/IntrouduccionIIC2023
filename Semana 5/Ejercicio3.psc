Proceso sin_titulo
	
	//9. Construir un programa que simule un men� de opciones para realizar las cuatro
//	operaciones aritm�ticas b�sicas (suma, resta, multiplicaci�n y divisi�n) con dos valores
//	num�ricos enteros. El usuario, adem�s, debe especificar la operaci�n con el primer
	//car�cter de la operaci�n que desea realizar: ?S' o ?s? para la suma, ?R? o ?r? para la resta, ?M?
//	o ?m? para la multiplicaci�n y ?D? o ?d? para la divisi�n.
	
	definir num1, num2, suma,resta,multiplicacion,division como entero
	definir operacion Como caracter
	
	Escribir "operaciones matematicas con dos numeros enteros"
	escribir "ingrese r/R para resta, S/s para suma, M/m para multiplicacion o d/D para division: "
	leer operacion
	
	escribir "el primer numero: "
	leer num1
	Escribir "ingrese el segundo numero: "
	leer num2
	
	Segun operacion Hacer
		's',"S":
			suma =(num1+num2)
			Escribir "el resultado de la suma es: " suma
		'r',"R":
			resta=(num1-num2)
			Escribir "el resultado de la resta es: " resta
		'd',"D":
			division=(num1/num2)
			escribir "el resultado de la division es: " division
		'm',"M":
			multiplicacion=(num1*num2)
			escribir "el resultado de la division es: " multiplicacion
		De Otro Modo:
			Escribir "ingrese un valor valido"
	Fin Segun
	
	
FinProceso


