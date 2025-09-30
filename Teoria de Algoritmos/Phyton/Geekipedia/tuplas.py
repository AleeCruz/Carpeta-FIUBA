print("Programa donde vamos a ver sobre las tuplas")
print("Las tuplas son elementos inmutables, es decir, no se pueden modificar")
#Tuplas
#Las tuplas siemprese  se definene con parentesis 
#Las tuplas son inmutables no podesmo cambiar susu valores como en una lista 

tupla = (1,2,3,4,5,6,7,8,9,10)

print(tupla)
 #Las tuplas puedene ser estructuras de datos heterogeneos
 
tupla_heterogenea = ("Alexander","Cruz",25,1.64,True,[100,150,300],"Alexander","Alexander")


print(tupla_heterogenea)
#Podriamos saber si un elemento esta dentro de tupla o no 

print(25 in tupla_heterogenea)

#tambien podriamos saber el elemento especifico a partir de un indice peculiar
print(tupla_heterogenea.index([100,150,300]))

#tambien podriamos saber l cantidad de veces que se repite un elemento de una tupla con 
#el metodo count

print(tupla_heterogenea.count("Alexander"))

#tambien pdoriamos saber la cantidad de elemeento s que tiene esta tuplan con la funcion
#len(tupla_heterogenea)

print(len(tupla_heterogenea))


#tambien exite la posibilidad de transformar una tupla a una lista con el metodo list
lista_heterogenea = list(tupla_heterogenea)

print(lista_heterogenea)
#La ventaja de las tuplas es que son mucho mas rapidas que las listas en tiempo de ejecucion
