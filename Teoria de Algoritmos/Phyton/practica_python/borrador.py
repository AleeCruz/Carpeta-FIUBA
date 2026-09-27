#Vamos a devolver la izquierda y la derecha de un arreglo que tiene solamente 3 elemento!
#Tenemos entonces lo siguiente 


def SMS(arreglo):
    if len(arreglo)==1:
        return arreglo
    
    med = len(arreglo)//2

    izq = arreglo[:med]#[6,7]
    der = arreglo[med:]#2,-1

    return izq,der


#QUe vamos a obtener si hago lo siguiente ?

arr = [6,7,2,-1]

print(SMS(arr))


#Las suposiciones que estamos haciendo son las correctas

#Cuando calculamos med = len(arre)//2
"""LOo que esta pasando es que testamos calculando el valor del indice done el elemento se encuentra en 
la mitad 


Que pasaria cuando enviamos un arreglo de 4 elemento ??
"""