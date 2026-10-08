def cambio_cambio_opt(monedas, x):
    # OPT[0] = 0
    OPT = [float('inf')] * (x + 1)
    OPT[0] = 0

    # Desde i = 1 a x
    for i in range(1, x + 1):
        minimo = float('inf')

        # Desde j = 1 a n (iterando sobre cada moneda en C)
        for c_j in monedas:
            # Corregimos 'X' del seudocódigo por 'i' (el subproblema actual)
            resto = i - c_j

            # si resto >= 0 y minimo > OPT[resto]
            if resto >= 0 and minimo > OPT[resto]:
                minimo = OPT[resto]

        # OPT[i] = 1 + minimo
        OPT[i] = 1 + minimo

    # Retornar OPT[x]
    return OPT[x]


# --- Ejemplo de uso ---
C = [1, 5, 6, 9]  # Monedas C
x = 11            # Monto x

resultado = cambio_cambio_opt(C, x)
print(f"OPT[{x}] = {resultado}")  # Imprime: OPT[11] = 2