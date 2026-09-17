"""Implementar una función que devuelva una lista de tuplas que represente todas las aristas del grafo>

a. Para un grafo dirigido

b. Para un grafo no dirigido, evitando devolver aristas repetidas

Métodos del grafo:
Grafo(es_dirigido = False, vertices_init = []) para crear un grafo no dirigido (hacer 'from grafo import Grafo')
Grafo(es_dirigido = True, vertices_init = []) para crear un grafo dirigido (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str"""



#se debe definir 2 tipos de funciones para la obtencion de una lista de tuplas
#Con las siguientes caracterisiticas


#How to search the vertex in graphs ??


def obtener_aristas_dirigidas(grafo):

    resultados = []
    for v in grafo:
        for w in grafo.adyacentes(v)
            resultados.append((v,w))

    retunr resultados


#Tecnicamente funciona??




#Deberiamos mempezar a realizar algunas operaciones con los grafos dirigidos
#implementacion de la obtencion de aristas de un grafo no dirigido
#Se debe tener un conjunto de visitados 
#Ademas de usar una lista



def obtener_aristas_dirigidos(grafo):
    resultados = []
    visitados = set() #Acabamos de crear un conjunto vacio para nuestro grafo
    for v in grafo:
        visitados.add(v)
        for w in grafo.adyacentes(v):
            if w not in visitados 
                resultados.append((v,w))
    return resultados
        