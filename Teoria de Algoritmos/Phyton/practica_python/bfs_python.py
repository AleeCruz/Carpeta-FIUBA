from collection import deque

##cositas importantes sobre la cola 
#Podremos desencolar de nuestra estructura cola con popleft()


def bfs(grado,origen):
    #Inicializacion de las estructuras basicas
    visitados={origen}
    padres = {origen:None}
    orden = {origen:0}

    #Vamos a utilizar el uso de deque como si fuera una cola 
    q = deque([origen])

    while q: #Esto tiene un significado especial "Mientras q no este vacia"

        v = q.popleft() #Procederemos a desencolar 

        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w] = v #padres.Guardar(w,v)
                orden[w] = orden[v]+1
                visitados.add(w)
                q.append(w)

        return padres, orden


"""Podriamos realizar  otra implementación con una condicion en el while mucho mas
explicita de lo que necesitamos"""



def bfs(grado,origen):
    #Inicializacion de las estructuras basicas
    visitados={origen}
    padres = {origen:None}
    orden = {origen:0}

    #Vamos a utilizar el uso de deque como si fuera una cola 
    q = deque([origen])

    while len(q)>0: #Esto tiene un significado especial "Mientras q no este vacia"

        v = q.popleft() #Procederemos a desencolar 
    
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w] = v #padres.Guardar(w,v)
                orden[w] = orden[v]+1
                visitados.add(w)
                q.append(w)

        return padres, orden