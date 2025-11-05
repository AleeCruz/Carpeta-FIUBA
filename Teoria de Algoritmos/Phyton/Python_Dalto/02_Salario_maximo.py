"""Se tiene una compañia que usa un registro de software para ver cual de todos los empleados 
tiene el salario mas alto el programa debe de terminar cuando el encargado de la compañia lo decida"""

salario = 0.0
maximo_salario = 0.0

condicional_bucle = "S"

while condicional_bucle == "S":
    
    salario = float(input("Ingrese el salario del empleado: "))
    
    if salario > maximo_salario:
        maximo_salario = salario
    
    print("\n")
    condicional_bucle = input("Desea ingresar otro empleado? S/N: ")
    
print("El salario mas alto es: ", maximo_salario)