#Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas el salario diario y el número de días trabajados. 
#Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.
salario_diario = float(input("Ingrese el salario diario del empleado: "))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))
salario_bruto = salario_diario * dias_trabajados
descuento_pension = salario_bruto * 0.10
descuento_salud = salario_bruto * 0.15
salario_neto = salario_bruto - descuento_pension - descuento_salud
print("El salario a pagar es:", salario_neto)