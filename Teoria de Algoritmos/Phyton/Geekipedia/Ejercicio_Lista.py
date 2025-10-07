def scheduling(charlas):
    charlas = sorted(charlas, key=lambda x: x[1])
    n = len(charlas)

    if n == 0:
        return []
    # Creamos listas indexadas desde 1 (posición 0 vacía)
    inicio = [0] + [c[0] for c in charlas]
    fin = [0] + [c[1] for c in charlas]
    valor = [0] + [c[2] for c in charlas]

    # p[j]: índice de la última charla que no se superpone con la j
    p = [0] * (n + 1)
    for j in range(1, n + 1):
        p[j] = 0
        for i in range(j - 1, 0, -1):
            if fin[i] <= inicio[j]:
                p[j] = i
                break

    # Programación dinámica
    M = [0] * (n + 1)
    for j in range(1, n + 1):
        M[j] = max(valor[j] + M[p[j]], M[j - 1])   # ← ecuación formal exacta

    # Reconstrucción de la solución óptima
    seleccionadas = []
    j = n
    while j > 0:
        if valor[j] + M[p[j]] > M[j - 1]:
            seleccionadas.append(charlas[j - 1])  # usamos charlas[j-1] porque charlas no tiene desplazamiento
            j = p[j]
        else:
            j -= 1

    seleccionadas.reverse()
    return seleccionadas

    
    

    
charlas = [
    (10, 12, 50),(11, 13, 80),(9, 10, 30),
    (14, 15, 60),(12, 14, 110),(15, 17, 70),(13, 16, 120)
]
    
print("La maxima ganancia es : ", scheduling(charlas))