print("Ejercicios sobre tuplas\n\n")


#Sucedera lo siguiente 
#Vamos a crear una tupla  que realice ciertas tareas que nosotros necesitamos
#Importante para crear una tupla  necesitamos declararla con unos parentesis


nombre_completo = ("Alexander","Cruz")

print(nombre_completo[0])
print(nombre_completo[1])


#Que pasaria si quisieramos realizar un cambio en nuestra tupla? por lo menos un dato

#nombre_completo[0] =" Fernando" //Esta linea de codigo no va a funcionar 



#Algo importante que acabamos de descubrir es que podemos asignar los valores de una 
#tupla a dos variables completamente distintas 


nombre, apellido = nombre_completo



print("\n\nSalto de linea para vizualizar los valores desde las variables definidas\n")
print(nombre)
print(apellido)