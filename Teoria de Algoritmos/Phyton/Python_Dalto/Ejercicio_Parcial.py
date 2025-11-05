apellido = ""
edad =0
dni =0
carrera = ""

apellido_dni_maximo = ""
maximo_dni = 0


condicion_bucle = "S"

cantidad_de_alumnos_ingresados = 0


while condicion_bucle == "S":
    
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    dni = int(input("Ingrese su DNI: "))
    carrera = input("Ingrese su carrera: ")

    #Incrementa el contador de la cantidad de alumnos ingresados
    cantidad_de_alumnos_ingresados += 1

    
    #apellido de maximo para el dni
    
    if dni > maximo_dni:
        maximo_dni = dni
        apellido_dni_maximo = apellido
    
    
    
    
    #es una variable de condicional que me permite saber si continuo o no con el bucle while
    condicion_bucle= input("Desea ingresar otro alumno? S/N: ")
    
    
    
    
print("Cantidad de alumnos ingresados: ", cantidad_de_alumnos_ingresados)
print("El apellido del alumno con el DNI mas alto es: ", apellido_dni_maximo)