"""Se tiene un encargado de un edificio que usa un software de registro de ingreso de 
personas a partir de su Nombre, se necesita saber la cantidad de personas que ingresaron al edificio"""

nombre = ""
condicional_bucle = "S"
cantidad_de_personas_ingresadas = 0



while condicional_bucle == "S":

    nombre = input("Ingrese su nombre: ")
    
    cantidad_de_personas_ingresadas += 1
    
    print("\n")
    condicional_bucle = input("Desea ingresar otra persona? S/N: ")
    
  
  
print("Cantidad de personas ingresadas: ", cantidad_de_personas_ingresadas)