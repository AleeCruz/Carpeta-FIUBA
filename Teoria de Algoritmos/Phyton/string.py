"""
Vamos a aprender sobre la concatenacion de strings 
"""
mensaje ="Hola"

espacio = " "

nombre = "Alexander"

print(mensaje+espacio+nombre)

#Vamos a ver otro ejemplo de strings 


"""
Aca vamos a ver otro ejemplo particular donde 
analizaresmo detalles particulare de los strings

"""


numero_uno = 3
numeor_dos = 6

resultado = numero_uno + numeor_dos

resultado = str(resultado)

print ("El reusltaod de la suma es: "+resultado)



#Otro ejemplo para usar varias cosas relacionadas a los string son 


mensaje = "Hola mi nombre es Alexander"

buscar_subcadena = mensaje.find("Alexander")

print(buscar_subcadena)




#Vamos a ver algo sobre extracciones de strings

mensaje = "Mi nombre es Alexander y voy a aprobar TDA"
extraer_subcadena = mensaje[2:19]

print(extraer_subcadena)




#Vamos a hablar sobre las comparaciones donde se ve el operador de comparacion


mensaje_uno = "Hola"
mensaje_dos = "Adios"

mensaje_uno == mensaje_dos

print(mensaje_uno == mensaje_dos)

