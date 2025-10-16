"""Dada un aula donde se pueden dar charlas.Las charlas tienen horario de inicio 
y de fin. Implementar un algoritmos Greedy que reciba un arreglo de los horarios
de las charlas, representado en tuplas los horarios de inicio, y sus horarios de fin
, e indique cuales son las charlas a dar para maximizar la cantidad total de 
charlas.
Indicar y justificar la complejidad del algoritmo Implementado """

def charlas(horarios):    
    orden_tiempo_fin = sorted(horarios, key=lambda x: x[1])
    
    if not orden_tiempo_fin:
        return []

    charlas_seleccionadas = [orden_tiempo_fin[0]]
    
    ultima_hora_fin = orden_tiempo_fin[0][1]
    
    for charla_actual in orden_tiempo_fin[1:]:
        
        hora_inicio_actual = charla_actual[0]
        
        if hora_inicio_actual >= ultima_hora_fin:
            
            charlas_seleccionadas.append(charla_actual)
            
            ultima_hora_fin = charla_actual[1]
    
    return charlas_seleccionadas


horarios  = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (5, 12), (6, 13), (8, 14), (12, 16)]

print(charlas(horarios)) 