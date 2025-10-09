def reconstruccion(G,M):
    elecciones =[]
    d = len(G)-1
    while (d>=0):
        opt_ayer= G[d-1] if d>0 else 0
        opt_anteayer = G[d-2] if d>1 else 0
        valor_hoy = M[d]
        if valor_hoy + opt_anteayer >= opt_ayer:
            elecciones.append(d)
            d -= 2
        else:
            d -= 1
    elecciones.reverse()
    return elecciones


def juan_el_vago(trabajos):
    dias = len(trabajos)
    M = trabajos
    G=[0]*dias
    G[0] = M[0]
    G[1] = max(M[0],M[1])

    for d in range(2,dias):
        G[d] = max(M[d] + G[d-2],G[d-1])
    return reconstruccion(G,M)

trabajos = [100,5,50,1,1,200]
print(juan_el_vago(trabajos))