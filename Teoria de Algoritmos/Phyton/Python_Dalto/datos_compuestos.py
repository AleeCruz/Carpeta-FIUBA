#Estamos viendo sobre los tipos de datos list o sea una lista
#Se leen de posiciones 0 1 2 3 4 5 ....
lista = ["GammaStream","Alexander",True,1.64]
print(lista)
print(lista[0])
#vamos a crear sobre los tipos de datos list 

lista_2=["Alexander",1.64,False,25]
lista_3=["Griselda",1.8,True,30]
print(lista_3[2])
print(lista_2[3])

#Vamos ahablar ahora sobre las tupla pertenecientes de python
tupla = ["GammaStream","Alexander",True,1.64]
print(tupla[3])

#Las listas son modificables porque son mutables, se pueden cambiar los elementos 
#por otros que queramos 

#Las tuplas son inmodificables , no se pueden cambiar sus valores predefinidoos
tupla =("Fernando","Cruz","Titular",24,13.0,False,True)

#Estas lineas de codigo no me permiten modificar la tupla
#tupla[1] =  "Gonzalez"
#tupla[3] = 25
print(tupla)
#Los conjuntos son tipos de datos compuestos en los cuales se usa llaves {} y para las tuplas


#Formando un conjunto en los cuales no aceptan datos repetidos
conjunto = {"Alexander",1.64,False,25,"Alexander",1.64}
print(conjunto)
#Los conjuntos se pueden redefinir pero no se pueden modificar los elementos de un conjunto
#conjunto[1] = 1.65
#conjunto[3] = 26
#print(conjunto)


#Bueno ahora vamos a ejercitar sobre los diccionarios

#Diccionarios 


diccionarios = {
    "Nombre": "Alexander",
    "Apellido": "Cruz Apaza",
    "Canal": "GammaStream",
    "Edad": 25,
    "Direccion": "Gregorio Laferre"
}

diccionarios["Direccion"] = "Valladolid"
print(diccionarios["Apellido"])
print(diccionarios["Canal"])
print(diccionarios["Direccion"])

#En resumen los diccionarios son un tipo de datos estructurados peculiares
#QUe nos permiten crear una estructura con clave: valor,
#Si tenemos varias claves tendremos varios valores
#y hay que separarla por ,(coma)