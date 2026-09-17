class GrafoPrueba:
    def __init__(self):
        # Diccionario que simula las conexiones: vértice -> lista de vecinos
        self.grafo = {
            "A": ["B", "C"],
            "B": ["A", "C"],
            "C": ["A", "B", "D"],
            "D": ["C"]
        }

    def obtener_vertices(self):
        return list(self.grafo.keys())

    def adyacentes(self, v):
        return self.grafo.get(v, [])

    def imprimir_vertices(grafo):
        for v in grafo.obtener_vertices():
             print(v)

# Instancia lista para usar en tus pruebas:

mi_grafo = GrafoPrueba()

mi_grafo.imprimir_vertices()



