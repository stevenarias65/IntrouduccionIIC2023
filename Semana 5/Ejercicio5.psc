Proceso sin_titulo
	//	Bucles Anidados
	//10. Una compa��a de seguros tiene contratados a n vendedores. Cada vendedor realiza
	//m�ltiples ventas a la semana. La pol�tica de pagos de la compa��a es que cada vendedor
	//recibe un sueldo base m�s un 10% extra por comisiones de sus ventas. El gerente de la
	//compa��a desea saber, por un lado, cu�nto dinero deber� pagar en la semana a cada
	//vendedor por concepto de comisiones de las ventas realizadas, y por otro lado, cu�nto
	//deber� pagar a cada vendedor como sueldo total (sueldo base + comisiones). Para cada
	//vendedor ingresar cuanto es su sueldo base, cuantas ventas realiz� y cuanto cobr� por
	//cada venta.
	
	definir sueldoBase, ventasRealizadas, precioVenta, vendedores, i, comision, sueldoTotal, j, sumaprecioventa Como Real
	
	Escribir "por favor digite la cantidad total"
	leer vendedores
	sumaprecioventa = 0
	
	i = 1
	Mientras i<=vendedores Hacer
		
		escribir "ingrese el sueldo base del vendedor ", i
		leer sueldoBase
		Escribir "ingrese las ventas realizadas por el vendedor ", i
		leer ventasRealizadas
		
		Para j=1 Hasta ventasRealizadas Con Paso 1 Hacer
			
			escribir "venta N� ", j
			leer precioVenta
			sumaprecioventa = sumaprecioventa + precioVenta
			
		Fin Para
		

		comision = (sumaprecioventa*(0.1))
		sueldoTotal = (sueldoBase + comision)
		Escribir "al vendedor ", i , " se le pagara de comision el total de $ ", comision " y su sueldo total durante la semana es de $ ", sueldoTotal
		
		
		
	
		i = i +1
		
	Fin Mientras
	
	
FinProceso
