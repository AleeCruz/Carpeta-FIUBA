nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
correo_electronico = input("Ingrese su correo electrónico: ")
nacionalidad = input("Ingrese su nacionalidad: ")
altura = float(input("Ingrese su altura (en metros): "))

print("\nInformación ingresada:")

print("Nombre completo:", nombre+" "+apellido)
print("Cantidad de caracteres en el nombre:", len(nombre))
print("Nombre en Mayusculas:", nombre.upper())

print("\n\n\n")

if edad >= 18:
    print("Registro exitoso.")
    print("Nombre completo:", nombre+" "+apellido)
    print("Edad:", edad)
    print("Correo electrónico:", correo_electronico)
    print("Nacionalidad:", nacionalidad)
    print("Altura:", altura, "metros")
else:
    print("Usted es menor de edad. \nNo se puede completar el registro.")

