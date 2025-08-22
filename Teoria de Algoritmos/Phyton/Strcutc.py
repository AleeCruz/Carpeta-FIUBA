from dataclasses import dataclass

@dataclass
class alumno: 
    nombre: str
    altura: float

alumnos = [
    alumno(nombre="Alexandder", altura=1.20),
    alumno(nombre="Sofia", altura=1.15),
    alumno(nombre="Bertao", altura=1.14),
    alumno(nombre="Yel", altura=1.12),
    alumno(nombre="Felipe", altura=1.02),
    alumno(nombre="Felix", altura=0.98),
    alumno(nombre="Ana", altura=1.18),
    alumno(nombre="Juan", altura=1.23)
]

def indice_mas_bajo(alumnos):
    izq, der = 0, len(alumnos) - 1
    
    while izq < der:
        mid = (izq + der) // 2
        
        if alumnos[mid].altura > alumnos[mid + 1].altura:
            # el mínimo está a la derecha
            izq = mid + 1
        elif alumnos[mid].altura > alumnos[mid - 1].altura:
            # el mínimo está a la izquierda
            der = mid - 1
        else:
            # encontramos el punto más bajo
            return mid
    
    return izq  # al final, izq == der y apunta al mínimo

def validar_mas_bajo(alumnos, indice):
    if indice == 0 or indice == len(alumnos) - 1:
        return False  # no puede estar en los extremos
    return (alumnos[indice].altura < alumnos[indice - 1].altura and
            alumnos[indice].altura < alumnos[indice + 1].altura)


# --- Prueba ---
i = indice_mas_bajo(alumnos)
print("Índice más bajo:", i, "| Alumno:", alumnos[i])
print("Validación:", validar_mas_bajo(alumnos, i))

