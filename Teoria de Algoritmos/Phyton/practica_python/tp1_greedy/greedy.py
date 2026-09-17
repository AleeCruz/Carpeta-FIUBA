from enum import Enum

class MonedaElegida(Enum):
    PRIMERA = "PRIMERA"
    ULTIMA = "ULTIMA"

def jugar(monedas):
    primer_moneda = 0
    ultima_moneda = len(monedas) - 1
    elecciones = []
    total_sophia = 0
    total_mateo = 0
    turno = 0

    while primer_moneda <= ultima_moneda:
        if turno % 2 == 0:  # Sophia: mayor o igual
            if monedas[primer_moneda] >= monedas[ultima_moneda]:
                elecciones.append(MonedaElegida.PRIMERA)
                total_sophia += monedas[primer_moneda]
                primer_moneda += 1
            else:
                elecciones.append(MonedaElegida.ULTIMA)
                total_sophia += monedas[ultima_moneda]
                ultima_moneda -= 1
        else:  # Mateo (elegido por Sophia): menor o igual
            if monedas[primer_moneda] <= monedas[ultima_moneda]:
                elecciones.append(MonedaElegida.PRIMERA)
                total_mateo += monedas[primer_moneda]
                primer_moneda += 1
            else:
                elecciones.append(MonedaElegida.ULTIMA)
                total_mateo += monedas[ultima_moneda]
                ultima_moneda -= 1

        turno += 1

    return elecciones, total_sophia, total_mateo


# --- EJECUCIÓN DE PRUEBAS ---
casos_de_prueba = [
    [2, 100, 1],
    [10, 1000, 5, 1],
    [5, 5, 5, 5],
    [4, 1, 2, 10]
]

for idx, monedas in enumerate(casos_de_prueba, 1):
    elecciones, sophia, mateo = jugar(monedas)
    
    print(f"--- Caso {idx}: {monedas} ---")
    print(f"Elecciones: {[e.value for e in elecciones]}")
    print(f"Total Sophia: {sophia}")
    print(f"Total Mateo:  {mateo}\n")