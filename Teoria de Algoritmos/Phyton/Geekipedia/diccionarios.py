#vamos a ver sobre  los Diccionarios en python 
#vamos a realizar varias operaciones con los diccionarios 

#La peculiaridad de los diccionarios es que tienen una clave y un valor 
diccionario = {}
print(diccionario)

#Vamos a crear un diccionario de 3 keys con 3 valores
diccionario = {"Blue":"Azul","Red":"Rojo","yellow":"amarrilo"}

print(diccionario)

#Para mostrar un elemento del diccionario podemos solo acceder por la clave 
print(diccionario["Blue"])
print(diccionario["yellow"])


#Para agregar un nuevo elemento al diccionario agregamos una nueva clave y ademas el
#Valor 
diccionario["Green"] = "Verde"

print(diccionario )

#En el caso de que necesitemo eliminar uno o varios elementos hacemos lo siguiente 

del(diccionario["Blue"])
print(diccionario)



diccionario = {"alexander":[22,2.64],"griselda":[18,1.50],"micaela":["none",1.40]}
print(diccionario)
print(diccionario["alexander"])