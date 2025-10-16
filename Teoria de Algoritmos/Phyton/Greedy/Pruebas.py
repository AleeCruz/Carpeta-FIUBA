
horarios  = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (5, 12), (6, 13), (8, 14), (12, 16)]

orden_tiempo_fin = sorted(horarios,key= lambda x: x[1])
print(orden_tiempo_fin)
#[(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (5, 12), (6, 13), (8, 14), (12, 16)]
#Actualmente esta ordenado por tiempo de fina todas las charlas 

#Se creo una nueva lista de seleccionados donde ingrese solamente la primera charla
charlas_seleccionadas = [orden_tiempo_fin[0]]

#Ahora mismo voy a guardar la hora de finalizacion de la primera charla seleccionada
ultima_hora_fin = orden_tiempo_fin[2][1]
print(ultima_hora_fin)

#Vamos a realizar un recorrido de cada una de las charlas sin incluir la primera
#porque ya la agregamos a la lsita de seleccionados
for charla in orden_tiempo_fin[1:]:
    hora_inicio_actual = charla[0] #Hora de inicio de la charla actual ( o sea el elemento de la posicion 1 de orden_tiempo_fin)
    
    if hora_inicio_actual >= ultima_hora_fin: #
        charlas_seleccionadas.append(charla) #Agrego la charla a la lista de seleccionados
        ultima_hora_fin = charla[1]
        

print(charlas_seleccionadas)