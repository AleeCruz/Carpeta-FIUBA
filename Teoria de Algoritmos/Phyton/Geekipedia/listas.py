#Vamos a ver ejeplos sobre la estructura de datos listas 
#Donde vamos a ver sobre listas homogeneas y heterogeneas
#El contenido se puede modificar 
lista = [] #Esta es una lista vacia
lista_homogenea = ["Alexander","yael","griselda","Hamilton","Micaela","Francisco"]
lista_heterogenea = ["Alexander",25,True,1.64,["a","b","c"],("x","y","z"),{"nombre":"Alexander","apellido":"Cruz"}]


print("Lista vacias")
listas_vacia = []
print(listas_vacia)

print("Listas homogeneas")
lista_homogenea = ["a","b","c","d","e","f"]
print(lista_homogenea)


print("Listas Heterogeneas")
listas_heterogeneas = ["Alexander",25,True,1.64,["a","b","c"],("x","y","z"),{"nombre":"Alexander","apellido":"Cruz"}]

print("Listas heterogeneas: ",listas_heterogeneas)

#Vamos a crear una lista de numeros decimales
print("Listahomogenea de numero decimales")
lista_decimales = [1.5,1.7,2.7,1.2,2.8]
print("Lista de numeros decimales: ",lista_decimales)

print("Lista heterogeneas de varios tipos de datos")
datos = ["Alexadner","Cruz",25,1.64,True]

print(datos)