"""
Subarreglo de máxima suma - Divide y Conquista
Ejecutar directamente en VSCode (F5 o botón de Run) para ver los resultados
en la terminal.
"""
""" for arreglo in arreglos_de_prueba:
        original = arreglo[:]  # copia para mostrar el arreglo original sin modificar
        resultado = max_subarray(arreglo)
        print(f"arreglo: {original}")
        print(f"  -> subarreglo de máxima suma: {resultado}  (suma = {sum(resultado)})")
        print()"""

def max_subarray(arr):
    longitud = len(arr)
    if (longitud == 1):
        return arr[0:]

    max_total = []

    mitad = longitud // 2

    max_izq = max_subarray(arr[:mitad])
    max_der = max_subarray(arr[mitad:])

    acumulado = arr[mitad]
    record = acumulado
    inicio_max_mitad = mitad
    fin_max_mitad = mitad

    for i in range(mitad - 1, -1, -1):
        acumulado += arr[i]
        if (acumulado > record):
            inicio_max_mitad = i
            record = acumulado

    acumulado = 0
    record = acumulado

    for i in range(mitad + 1, longitud):
        acumulado += arr[i]
        if (acumulado > record):
            fin_max_mitad = i
            record = acumulado

    max_mid = arr[inicio_max_mitad:fin_max_mitad + 1]

    if (sum(max_izq) > sum(max_der)):
        max_total = max_izq
    else:
        max_total = max_der

    if (sum(max_mid) > sum(max_total)):
        max_total = max_mid

    return max_total


# ---------------------------------------------------------
# ARREGLOS DE PRUEBA
# Agregá, editá o comentá los que quieras probar
# ---------------------------------------------------------
"""arreglos_de_prueba = [
    [5, 3, 2, 4, -1],              # ejemplo 1 del enunciado -> [5, 3, 2, 4]
    [5, 3, -5, 4, -1],             # ejemplo 2 del enunciado -> [5, 3]
    [5, -4, 2, 4, -1],             # ejemplo 3 del enunciado -> [5, -4, 2, 4]
    [5, -4, 2, 4],                 # ejemplo 4 del enunciado -> [5, -4, 2, 4]
    [-3, 4, -1, 2, 1, -5],         # ejemplo 5 del enunciado -> [4, -1, 2, 1]

    [1],                           # un solo elemento positivo
    [-1],                          # un solo elemento negativo
    [0],                           # un solo elemento cero
    [-5, -3, -8, -1],              # todos negativos -> el "menos malo"
    [7, 7, 7, 7],                  # todos iguales
    [1, -1, 1, -1, 1],             # alternado
    [100, -1, -1, -1, 100],        # dos picos separados por negativos chicos
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # ejemplo clásico de Kadane -> [4, -1, 2, 1]
]"""


# ---------------------------------------------------------
# EJECUCIÓN: corre la función sobre cada arreglo de prueba
# ---------------------------------------------------------
if __name__ == "__main__":
   
         # Para probar con tu propio arreglo, descomentá y editá estas líneas:
    mi_arreglo = [2,-1]
    print("Mi propio arreglo:", mi_arreglo)
    print("Resultado:", max_subarray(mi_arreglo))
    print()
   