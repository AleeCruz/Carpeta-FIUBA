
#Vamos a ver sobre las listas y como operarlas

my_list = ["python",35,True,"Alexander",3.14]

print(type(my_list))

print(my_list[3])

#vamos a ver como agregar elementos a una lista con un simple apppend()

my_list.append("Nuevo elemento")
print(my_list)


#Podriamos utilizar otra manera de agregar elementos a una lista 

my_list.insert(3,"GammaStream")
print(my_list)


#Tambien debemos ver la manera de eliminar objetos de una lista
#El mensaje .remove() me permite eliminar el objeto que nosotros queramos 
my_list.remove("Alexander")
print(my_list)

#tambien vamos a ver como eliminar un objeto por el indice con el metodo pop()
print(my_list.pop(3))
print(my_list)

print(my_list.count("True"))

my_list.reverse()

print(my_list)