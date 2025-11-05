"""Se tiene el ingreso de varios edades de personas, se necesita saber la cantidad de edades
pares que se ingresaron en un programa de software de registro de edades"""




edad = 0

condicional_bucle = "S"

cantidad_edades_pares = 0


while condicional_bucle == "S":
    
    print("\n")
    edad = int(input("Ingrese su edad: "))
    
    if edad % 2 == 0:
        cantidad_edades_pares += 1
    
    condicional_bucle = input("Desea ingresar otra edad? S/N: ")
    

print("Cantidad de edades pares ingresadas: ", cantidad_edades_pares)