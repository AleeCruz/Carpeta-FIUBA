print("vamos a ejecutar un nuevo programa")

equipo = {8:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",10:"Lionel Messi"}

print(equipo)
#Podriamos acceder a varios elementos a traves del indice o en otras palabras la clave

print(equipo[8])
print(equipo[11])
print(equipo[10])
#Si yo ejecutara la siguiente linea de codigo me apareceria un error al momento de 
#ejecutarse todo el programa
#print(equipo[200]) porque no exite tal clave en el diccionario

#Podriamos evitar este tipo de errores con un metodo get propio de los diccionarios 
print(equipo.get(10,"No existe un jugador con ese dorsal"))
#Suponiendo que quiera acceder a un elemento invalido podria ejecutar el error
print(equipo.get(200,"No existe tal jugador por ese numero de clave "))

#Podriamos imprimir las claves unicamente de los diccionarios
print(equipo.keys())

#Ahora bien que pasaria si solo quisiera los valores pertenecientes en los diccionarios 
print(equipo.values())


#Tambien hay otra forma de mostrar los diccionarios del siguiente modo, como
#si fuera simplemente una lista 
print(equipo.items())
print(len(equipo))
