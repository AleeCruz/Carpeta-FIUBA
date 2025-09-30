print("Nuevo programa")

#Habaremos sobrelas operaciones que se pueden relaizar sobre unos conjuntos 
#Podriamos crear conjunto directamente con valores 
#En ese caso ya no haria falta agregar el inicializador set() para indicar 
#de que se trata de un conjunto vacio

a ={1,2,3}
b = {4,5,3,2}
#n este caso los conjunto no estan ordenados por lo tanto 
#al hacer la comparacion de ambos conjunto veremos que sus elementos son 
#Iguales a pesar de que no tengan el mismo orden
print(a == b)
print(len(a))
print(len(b))

#Podemos hablar sobre la union de 2 conjuntos distintos 

c = a | b
print(c)

#Si quisieramos analizar la interseccion de los conjunto a y b solo tendriamos 
#que utilizar el simbolo de ampersan &

c = a & b

print(c)


#tambien podriamos hablar sobre la diferencia que exite entre a y b 
#como los elementos que estan presentes en a pero no en b
#tambien podriamos pensar a los elementos que estan en b pero no en a 


c = a-b
print (c)

c = b-a

print(c)


#tambien podriamos pensar sobre la diferencia simetrica, o sea los elementos que 
#propios que no cmparten ni a ni b 

c = a^b

print(c)


#Veamos ahora si un subconjunto pertenece o no a otro conjunto 
#En este caso tenemos que 
a = {1,2,3}
b={4,5,6}
c={1,2,3,4,5,6,7,8,9}

print(b.issubset(c))
