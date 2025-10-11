
def sche_solucion(M_SCHE, valor, p, j, solucion):
    if j == 0:
        return solucion
    if valor[j] + M_SCHE[p[j]] >= M_SCHE[j - 1]:
        solucion.append(j)
        return sche_solucion(M_SCHE, valor, p, p[j], solucion)
    else:
        return sche_solucion(M_SCHE, valor, p, j - 1, solucion)



def scheduling(charlas):
    # Ordenamos por hora de finalización
    scheduling_ordenado = sorted(charlas, key=lambda x: x[1])
    n = len(scheduling_ordenado)

    # Indexamos desde 1
    inicios = [0] + [x[0] for x in scheduling_ordenado]
    finalizaciones = [0] + [x[1] for x in scheduling_ordenado]
    valores = [0] + [x[2] for x in scheduling_ordenado]

    # Calcular p[j] = última charla compatible con j
    p = [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(j - 1, 0, -1):
            if finalizaciones[i] <= inicios[j]:
                p[j] = i
                break

    # Programación dinámica: construir M_SCHE
    M_SCHE = [0] * (n + 1)
    for j in range(1, n + 1):
        M_SCHE[j] = max(valores[j] + M_SCHE[p[j]], M_SCHE[j-1])

    # Recuperar las charlas seleccionadas
    solucion_indices = sche_solucion(M_SCHE, valores, p, n, [])
    solucion_indices.reverse()

    # Traducimos índices a charlas
    seleccionadas = [scheduling_ordenado[i - 1] for i in solucion_indices]

    return seleccionadas
