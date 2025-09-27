"""Se realizara un programa correspondiente a cadenas de texto puntualmente a la concatenacion 
de cadenas de texto """

print("Nuevo Programa")

mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"

print(mensaje)

#Ahora se procedera a ver un ejemplo de programacion de concatenacion de strings
mensaje = "Hola"
espacio = " "
nombre = "Alexaeder"
print(mensaje + espacio + nombre)

#Vamos a ver la concatenacion de cadenas de texto con variables de tipo int y strings
numero_1 =10
numero_2 = 25
resultado = numero_1 + numero_2
print("El resultado de la suma es : " + str(resultado)) 

#Vamos a ver lo que es una busqeuda en unsa cadena de caracteres 
print("Busqueda: ")
mensaje = "Hola Alexadner Como estas?"
buscar_subcadena = mensaje.find("Alexadner")
print(buscar_subcadena)


#Ahora vamos a ver en que consiste la extraccioon 
print("Extraccion:")
mensaje = "Hola Alexander como estas ?"
extraer_subcadena = mensaje[5:17]
print(extraer_subcadena)

"""Bueno hasta ahora hemos aprendidio varias cosas conrespecto a las cadenas de 
caracteres o emjor conocidos como strings de python """
#Comparacion se utiliza unicamente para poder comparar 2 cadenas de tecto con lo
#cual se utiliza el comparador ==
print("Comparacion en cadenas de texto")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
comparacion = mensaje_uno == mensaje_dos
print(comparacion)

mensaje_uno = "Hola"
mensaje_dos = "Adios"
comparacion= mensaje_uno ==mensaje_dos
print (comparacion)