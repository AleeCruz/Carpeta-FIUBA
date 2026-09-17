#Para empezar como se realizan los recorridos de BSF en un grafo no dirigido??


"""El codigo mostrado a continuacion esta descrito para el lenguaje de programacion
GOlang"""
def bfs(grafo,origen):
    padres[origen] = None
    orden[origen] = 0 #orden.Guardar(origen,0)
    visitados.add(origen)
    q = Cola()
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w]=v
                orden[w] = orden[v]+1
                visitados.add(w)
                q.encolar(w)
    
    return padres,orden 


    """Ahora tendremos que realizar lo siguiente!, implementar las misma 
    funcionalidad para python veremos que sucede"""


from collections import deque

def bfs(grafo, origen):
    # Inicialización de estructuras
    padres = {origen: None}
    orden = {origen: 0}
    visitados = {origen}
    
    # Uso de deque como cola de FIFO eficiente
    q = deque([origen])
    
    while q:
        v = q.popleft()  # Desencolar
        
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                q.append(w)  # Encolar
                
    return padres, orden






    