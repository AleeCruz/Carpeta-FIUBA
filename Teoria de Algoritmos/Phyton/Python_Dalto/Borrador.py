apellido = ""
edad = 0
dni = 0
carrera = ""
cantidad_alumnos_ingresados = 0

condicional = 'S'

while condicional == 'S':
    
    #Lectura de datos 
    apellido = input("Ingrese el apellido del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    dni = int(input("Ingrese el DNI del alumno: "))
    carrera = input("Ingrese la carrera del alumno: ")
    
    cantidad_alumnos_ingresados += 1
    
    
    print("\n")
    
    condicional = input("Deseas continuar ? S/N: ")
    

printf(cantidad_alumnos_ingresados)