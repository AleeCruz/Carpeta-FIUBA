print("Programa sobre los conjuntos en python ")
#Para empezar como se inicializan los conjuntos ??
#Hay que indicar que que los conjunto se inicializan son set()
#caso contrario estariamos inicializando un diccionario
#Ademas los conjunto se inicializan con llaves similar a los diccionarios 
#pero hay que especificar  la instruccion set()

conjunto_1 = set()
#Podriamos empezar agregando varios elementos heterogeneos a los conjunto 
#Los conjuntos no admiten elementos duplicados ademas que no se pueden agreagar 
#listas o diccionarios porque son mutables, los conjunto son inmutables
conjunto_1 = {1,2,3,"Alexander","cruz",25,True,16.9}

print(conjunto_1)

#Podriamos realizar varias operaciones para los conjuntos 
#Podemos inclusive realzar inclusive insercciones hacia los conjuntos con el m
#el metodo add()
conjunto_1.add("Nuevo elemento")
conjunto_1.add("Agregue nuevo elemento")
conjunto_1.add(25)
conjunto_1.add(3.1415673)

print(conjunto_1)

#Ahora bien podriamos conocer varias cosas sobre los conjuntos 
#Podemos elmininar elementos particulares de los conjuntos
conjunto_1.remove("Alexander")

print(conjunto_1)