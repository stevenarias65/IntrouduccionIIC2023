Proceso sin_titulo
	//	Bucles Anidados
	//10. Una compañía de seguros tiene contratados a n vendedores. Cada vendedor realiza
	//múltiples ventas a la semana. La política de pagos de la compañía es que cada vendedor
	//recibe un sueldo base más un 10% extra por comisiones de sus ventas. El gerente de la
	//compañía desea saber, por un lado, cuánto dinero deberá pagar en la semana a cada
	//vendedor por concepto de comisiones de las ventas realizadas, y por otro lado, cuánto
	//deberá pagar a cada vendedor como sueldo total (sueldo base + comisiones). Para cada
	//vendedor ingresar cuanto es su sueldo base, cuantas ventas realizó y cuanto cobró por
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
			
			escribir "venta N° ", j
			leer precioVenta
			sumaprecioventa = sumaprecioventa + precioVenta
			
		Fin Para
		

		comision = (sumaprecioventa*(0.1))
		sueldoTotal = (sueldoBase + comision)
		Escribir "al vendedor ", i , " se le pagara de comision el total de $ ", comision " y su sueldo total durante la semana es de $ ", sueldoTotal
		
		
		
	
		i = i +1
		
	Fin Mientras
	
	
FinProceso
